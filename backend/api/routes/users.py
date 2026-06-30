from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class UserProfileResponse(BaseModel):
    success: bool
    message: str
    data: dict | None = None


@router.get("/profile", response_model=UserProfileResponse)
async def profile(user_id: str):
    raise HTTPException(status_code=501, detail="User profile not implemented yet")
