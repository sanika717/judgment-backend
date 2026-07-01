from fastapi import APIRouter
from fastapi import Depends

from api.dependencies import (
    get_current_user
)

router = APIRouter()


@router.get("/")
def profile(
    user=Depends(get_current_user)
):

    return {
        "success": True,
        "data": {
            "id": user.id,
            "name": user.username,
            "email": user.email
        }
    }