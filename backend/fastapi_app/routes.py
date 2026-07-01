# backend/fastapi_app/routes.py

import os, uuid
from fastapi import APIRouter, UploadFile, Form, File, Query, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from gtts import gTTS
from dotenv import load_dotenv
load_dotenv()

from config import USER_DATA_DIR
from database import (
    file_record_exists,
    insert_file_record,
    delete_user_file_record,
    list_user_files,
    insert_new_session
)
from chat_history_db import (
    get_user_chat_history,
    save_user_chat_history,
    get_all_sessions
)
from backend.services.document.doc_utils import process_single_doc, load_user_vectorstore
from backend.vector_store.vectorstore import delete_file_embeddings
from rag_pipeline import build_rag_chain

router = APIRouter()

def get_user_dirs(user_id: str):
    user_dir = os.path.join(USER_DATA_DIR, user_id)
    pdf_dir = os.path.join(user_dir, "pdfs")
    vectorstore_dir = os.path.join(user_dir, "vectorstore")
    os.makedirs(pdf_dir, exist_ok=True)
    os.makedirs(vectorstore_dir, exist_ok=True)
    return user_dir, pdf_dir, vectorstore_dir


# -------------------- Session --------------------
@router.post("/create-session")
def create_session(user_id: str = Query(...)):
    session_id = str(uuid.uuid4())
    insert_new_session(user_id, session_id)
    return {"session_id": session_id}


# -------------------- Upload & Index --------------------
@router.post("/upload")
async def upload_file(
    user_id: str = Form(...),
    session_id: str = Form(...),
    file: UploadFile = File(...)
):
    user_dir, pdf_dir, vectorstore_dir = get_user_dirs(user_id)
    filepath = os.path.join(pdf_dir, file.filename)
    namespaced_user = f"{user_id}"

    if not file_record_exists(namespaced_user, file.filename, session_id):
        with open(filepath, "wb") as f:
            f.write(await file.read())
        insert_file_record(namespaced_user, file.filename, session_id)

        try:
            process_single_doc(
                user_id=user_id,
                filename=file.filename,
                pdf_dir=pdf_dir,
                vectorstore_dir=vectorstore_dir,
                user_dir=user_dir,
                session_id=session_id
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to index file: {e}")
        return {"message": f"{file.filename} uploaded and indexed"}

    return JSONResponse(content={"message": f"{file.filename} already exists in session"}, status_code=400)


# -------------------- File Listing --------------------
@router.get("/list-files")
def list_files(user_id: str = Query(...), session_id: str = Query(...)):
    try:
        files = list_user_files(user_id, session_id)
        return {"files": files}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# -------------------- Chat with RAG --------------------
@router.post("/chat")
async def chat(user_id: str = Form(...), session_id: str = Form(...), message: str = Form(...)):
    try:
        user_dir, pdf_dir, vectorstore_dir = get_user_dirs(user_id)
        retriever = load_user_vectorstore(user_id, vectorstore_dir)
        if not retriever:
            return JSONResponse(content={"error": "No embeddings found"}, status_code=404)

        history = get_user_chat_history(user_id, session_id)
        chain = build_rag_chain(retriever, history)

        try:
            reply = chain.invoke({"question": message})
        except Exception as e:
            # Handle Ollama connection errors gracefully
            if "Connection refused" in str(e) or "ConnectError" in str(e):
                return JSONResponse(
                    content={"error": "Ollama server not reachable. Please start Ollama (run `ollama serve`) and try again."},
                    status_code=503,
                )
            raise e  # re-raise unexpected errors

        save_user_chat_history(user_id, session_id, message, reply)
        return {"reply": reply}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# -------------------- TTS Utility --------------------
def text_to_speech(user_id: str, session_id: str, text: str, tts_dir: str) -> str:
    filename = f"{session_id}_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(tts_dir, filename)
    tts = gTTS(text=text, lang="en")
    tts.save(filepath)
    return filepath

