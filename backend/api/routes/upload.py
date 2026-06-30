from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel

router = APIRouter()

class UploadResponse(BaseModel):
    success: bool
    message: str
    data: dict | None = None


@router.post("/pdf", response_model=UploadResponse)
async def upload_pdf(user_id: str = Form(...), session_id: str = Form(...), file: UploadFile = File(...)):
    raise HTTPException(status_code=501, detail="Upload pipeline not implemented yet")
