from sqlalchemy.orm import Session

from models.chat import Chat


class ChatRepository:

    @staticmethod
    def create(
        db: Session,
        chat: Chat
    ):
        db.add(chat)
        db.commit()
        db.refresh(chat)

        return chat

    @staticmethod
    def get_by_id(
        db: Session,
        session_id: int
    ):
        return (
            db.query(Chat)
            .filter(Chat.id == session_id)
            .first()
        )

    @staticmethod
    def get_user_sessions(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Chat)
            .filter(Chat.user_id == user_id)
            .all()
        )