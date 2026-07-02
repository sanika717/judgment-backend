from fastapi import APIRouter, Depends

from api.dependencies import get_current_user # adjust path if different

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

@router.get("/")
def profile(
    current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }