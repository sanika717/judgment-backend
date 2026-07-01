from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.session import get_db

from api.dependencies import (
    get_current_user
)

from services.chat.session_service import (
    SessionService
)

router = APIRouter()


@router.post("/create")
def create_session(
    title: str,
    document_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    session = (
        SessionService.create_session(
            db=db,
            user_id=user.id,
            title=title,
            document_id=document_id
        )
    )

    return {
        "success": True,
        "session_id": session.id
    }