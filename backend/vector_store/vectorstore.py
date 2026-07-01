# backend/src/vectorstore.py
import os
import shutil
import sqlite3
from langchain.indexes import SQLRecordManager, index
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


# Initialize embeddings globally (same as doc_utils)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


class VectorDB:
    def __init__(self, vectorstore):
        self.client = vectorstore
        self.record_manager = None

    def create_record_manager(self, db_url, name):
        """Initialize the SQLRecordManager for tracking indexed documents."""
        self.record_manager = SQLRecordManager(namespace=name, db_url=db_url)
        self.record_manager.create_schema()

    def index_documents(self, documents, source_id_key="source"):
        """Index documents into the vectorstore, using source_id_key as metadata field."""
        if not self.record_manager:
            raise ValueError("Record manager not initialized. Call create_record_manager() first.")
        return index(
            documents,
            self.record_manager,
            self.client,
            cleanup=None,
            source_id_key=source_id_key,
        )

    def get_retriever(self):
        """Return a retriever interface from the vectorstore."""
        return self.client.as_retriever(search_kwargs={"k": 5})


def delete_vectorstore(vectorstore_dir):
    """Delete the entire vectorstore (not recommended unless removing user fully)."""
    shutil.rmtree(os.path.join(vectorstore_dir, "main"), ignore_errors=True)


def delete_file_embeddings(user_id: str, vectorstore_dir: str, user_dir: str, filename: str, session_id: str):
    """
    Delete all embeddings associated with a specific file+session_id from the user's vectorstore.
    Also removes associated records from the SQLite record manager.
    """
    # Compute unique source_id
    source_id = f"{filename}:{session_id}".lower().strip()

    # Path to user's vectorstore
    vectorstore_path = os.path.join(vectorstore_dir, user_id)

    # Initialize Chroma with HuggingFace embeddings
    vectordb = Chroma(
        collection_name="main",
        persist_directory=vectorstore_path,
        embedding_function=embeddings
    )

    print("Before delete:", vectordb._collection.count())

    # Get all embeddings metadata
    results = vectordb.get(include=["metadatas"])
    all_metadatas = results["metadatas"]
    all_ids = vectordb._collection.get()["ids"]

    # Find ids with matching source
    source_ids_to_delete = [
        id_ for id_, meta in zip(all_ids, all_metadatas)
        if meta.get("source", "").lower().strip() == source_id
    ]

    # Delete those vectors
    if source_ids_to_delete:
        vectordb.delete(ids=source_ids_to_delete)
        vectordb.persist()
        print("Deleted vectors:", len(source_ids_to_delete))
    else:
        print(f"[INFO] No embeddings found for {source_id}")

    print("After delete:", vectordb._collection.count())

    # Remove records from record_manager.db
    db_path = os.path.join(user_dir, "record_manager.db")
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM upsertion_record WHERE group_id = ?", (source_id,))
            conn.commit()
        print(f"[INFO] record_manager.db cleaned for {source_id}")
    except Exception as e:
        print(f"[ERROR] Failed to clean record_manager.db: {e}")
