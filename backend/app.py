import os
import io
import math
import uuid
from typing import List, Dict

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import numpy as np
import cv2

from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from local_llm_client import get_embedding

load_dotenv()

BASE_DATA_DIR = "user_data"
os.makedirs(BASE_DATA_DIR, exist_ok=True)

# ========== UTIL: IMAGE PREPROCESSING ==========
def preprocess_pil_image(pil_img: Image.Image) -> Image.Image:
    """Preprocess image for better OCR results."""
    arr = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 9, 75, 75)
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return Image.fromarray(th)

# ========== UTIL: OCR ==========
def ocr_pdf_to_pages(pdf_path: str, dpi: int = 300) -> List[str]:
    """Convert PDF to images and OCR with Tesseract."""
    pil_pages = convert_from_path(pdf_path, dpi=dpi)
    page_texts: List[str] = []

    for i, pil in enumerate(pil_pages):
        preprocessed = preprocess_pil_image(pil)
        try:
            text = pytesseract.image_to_string(preprocessed, lang="eng+hin")
            text = text.strip()
        except Exception as e:
            print(f"[ERROR] Tesseract OCR failed for page {i+1}: {e}")
            text = ""
        page_texts.append(text)
    return page_texts

# ========== UTIL: SIMPLE CHUNKER ==========
def split_text_to_chunks(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    if not text:
        return []
    chunks: List[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap if (end - overlap) > 0 else end
    return chunks

# ========== UTIL: Chroma helpers ==========
def get_user_vectordb(user_id: str):
    """Get (or create) a persistent Chroma DB for a user."""
    user_dir = os.path.join(BASE_DATA_DIR, user_id)
    vectordb_dir = os.path.join(user_dir, "vectorstore")
    os.makedirs(vectordb_dir, exist_ok=True)

    vectordb = Chroma(
        collection_name="main",
        persist_directory=vectordb_dir,
        embedding_function=None  # manual embeddings
    )
    return vectordb

# ========== FASTAPI APP ==========
app = FastAPI(title="OCR → Ollama Embeddings → Retrieval")

@app.post("/upload")
async def upload_and_index(user_id: str = Form(...), file: UploadFile = File(...)):
    """Upload a PDF → OCR → Chunk → Embed (Ollama) → Store in Chroma."""
    user_dir = os.path.join(BASE_DATA_DIR, user_id)
    pdf_dir = os.path.join(user_dir, "pdfs")
    os.makedirs(pdf_dir, exist_ok=True)

    save_name = f"{uuid.uuid4().hex}_{file.filename}"
    pdf_path = os.path.join(pdf_dir, save_name)
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    # 1) OCR
    page_texts = ocr_pdf_to_pages(pdf_path)
    if not page_texts:
        raise HTTPException(status_code=400, detail="No pages extracted")

    # 2) Chunk + Embed
    texts, metadatas, ids = [], [], []
    source_id = save_name
    for page_no, page_text in enumerate(page_texts, start=1):
        chunks = split_text_to_chunks(page_text)
        for i, chunk in enumerate(chunks):
            texts.append(chunk)
            metadatas.append({"source": source_id, "page": page_no, "chunk_index": i})
            ids.append(f"{source_id}-{page_no}-{i}")

    embeddings = [get_embedding(t) for t in texts]

    # 3) Save to Chroma
    vectordb = get_user_vectordb(user_id)
    vectordb._collection.add(embeddings=embeddings, documents=texts, metadatas=metadatas, ids=ids)
    vectordb.persist()

    return {"message": "uploaded and indexed", "file_id": source_id, "chunks_indexed": len(texts)}

@app.post("/query")
async def query(user_id: str = Form(...), query_text: str = Form(...), top_k: int = Form(5)):
    """Query user's vectorstore with Ollama embeddings."""
    vectordb = get_user_vectordb(user_id)

    try:
        col_count = vectordb._collection.count()
    except Exception:
        col_count = 0
    if col_count == 0:
        return JSONResponse(content={"error": "No indexed vectors for this user"}, status_code=404)

    q_embedding = get_embedding(query_text)

    results = vectordb._collection.query(
        query_embeddings=[q_embedding],
        n_results=top_k,
        include=["metadatas", "documents", "distances", "ids"]
    )

    matches = []
    for idx, doc_id in enumerate(results.get("ids", [[]])[0]):
        matches.append({
            "id": doc_id,
            "text": results.get("documents", [[]])[0][idx],
            "metadata": results.get("metadatas", [[]])[0][idx],
            "distance": results.get("distances", [[]])[0][idx]
        })

    return {"query": query_text, "matches": matches}

@app.get("/health")
def health():
    return {"status": "ok"}
