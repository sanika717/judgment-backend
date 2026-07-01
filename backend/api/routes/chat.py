from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.session import get_db

from schemas.chat import ChatRequest

from services.chat.chat_service import (
    ChatService
)

router = APIRouter()


@router.post("/")
async def chat(
    payload: ChatRequest,
    db: Session = Depends(get_db)
):

    try:

        answer = ChatService.ask(
            db=db,
            document_id=payload.document_id,
            session_id=payload.session_id,
            question=payload.question,
            language=payload.language
        )

        return {
            "success": True,
            "data": {
                "answer": answer
            }
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )