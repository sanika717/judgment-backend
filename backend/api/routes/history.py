from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.session import get_db

from repositories.message_repository import (
    MessageRepository
)

router = APIRouter()


@router.get("/{session_id}")
def get_chat_history(
    session_id: int,
    db: Session = Depends(get_db)
):

    messages = (
        MessageRepository
        .get_session_messages(
            db,
            session_id
        )
    )

    return {
        "success": True,
        "data": messages
    }