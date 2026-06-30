from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class DocumentListResponse(BaseModel):
    success: bool
    message: str
    data: dict | None = None


@router.get("/", response_model=DocumentListResponse)
async def list_documents(user_id: str):
    raise HTTPException(status_code=501, detail="Document listing not implemented yet")
