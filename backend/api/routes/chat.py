from fastapi import APIRouter, Form, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ChatResponse(BaseModel):
    success: bool
    message: str
    data: dict | None = None


@router.post("/query", response_model=ChatResponse)
async def query(user_id: str = Form(...), session_id: str = Form(...), message: str = Form(...)):
    raise HTTPException(status_code=501, detail="Chat query not implemented yet")
