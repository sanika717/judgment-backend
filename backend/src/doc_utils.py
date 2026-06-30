import os
from typing import List
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from src.ocr_utils import ocr_pdf_to_pages   # ✅ use local OCR (Tesseract)

# Env setup
load_dotenv()

HF_EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=HF_EMBED_MODEL)

# ---------- File loader + splitter ----------
def _load_file_chunks(fpath: str, source_id: str, ocr_dpi: int = 300, ocr_threshold: int = 200) -> List[Document]:
    ext = os.path.splitext(fpath)[1].lower()
    pages: List[Document] = []

    if ext == ".csv":
        loader = CSVLoader(file_path=fpath)
        pages = loader.load()

    elif ext == ".pdf":
        try:
            loader = PyPDFLoader(fpath)
            pages = loader.load()
        except Exception as e:
            print(f"[WARN] PyPDFLoader failed: {e}")
            pages = []

        total_len = sum(len(getattr(p, "page_content", "")) for p in pages)
        if not pages or total_len < ocr_threshold:
            texts = ocr_pdf_to_pages(fpath, dpi=ocr_dpi)
            pages = [Document(page_content=t, metadata={"source": source_id, "page": i+1}) for i, t in enumerate(texts)]

    # Normalize
    normalized = []
    for p in pages:
        content = getattr(p, "page_content", str(p))
        meta = getattr(p, "metadata", {})
        if "source" not in meta:
            meta["source"] = source_id
        normalized.append(Document(page_content=content, metadata=meta))

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(normalized)

# ---------- Main Processing ----------
def process_single_doc(user_id: str, filename: str, pdf_dir: str, vectorstore_dir: str, user_dir: str, session_id: str):
    fpath = os.path.join(pdf_dir, filename)
    source_id = f"{filename}:{session_id}"
    chunks = _load_file_chunks(fpath, source_id)
    if not chunks:
        print(f"[WARN] No content found in {filename}")
        return

    texts = [c.page_content for c in chunks]
    metadatas = [c.metadata for c in chunks]
    ids = [f"{source_id}-{i}" for i in range(len(texts))]

    vectordb = Chroma(
        collection_name="main",
        persist_directory=os.path.join(vectorstore_dir, user_id),
        embedding_function=embeddings
    )

    vectordb.add_texts(texts, metadatas=metadatas, ids=ids)
    vectordb.persist()
    print(f"[INFO] Indexed {len(texts)} chunks for {filename} (session {session_id})")

def load_user_vectorstore(user_id: str, vectorstore_dir: str):
    path = os.path.join(vectorstore_dir, user_id)
    if not os.path.exists(path):
        return None
    vectordb = Chroma(
        collection_name="main",
        persist_directory=path,
        embedding_function=embeddings
    )
    return vectordb.as_retriever(search_kwargs={"k": 10})
