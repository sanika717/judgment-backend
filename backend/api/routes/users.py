from fastapi import APIRouter
from fastapi import Depends

from api.dependencies import (
    get_current_user
)

router = APIRouter()


@router.get("/me")
def current_user(
    user=Depends(
        get_current_user
    )
):

    return {
        "success": True,
        "data": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }
    }