from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class HistoryResponse(BaseModel):
    success: bool
    message: str
    data: dict | None = None


@router.get("/sessions", response_model=HistoryResponse)
async def sessions(user_id: str):
    raise HTTPException(status_code=501, detail="History sessions listing not implemented yet")
