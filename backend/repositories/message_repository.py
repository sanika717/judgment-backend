from sqlalchemy.orm import Session

from models.message import Message


class MessageRepository:

    @staticmethod
    def create(
        db: Session,
        message: Message
    ):
        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    @staticmethod
    def get_session_messages(
        db: Session,
        session_id: int
    ):
        return (
            db.query(Message)
            .filter(
                Message.session_id == session_id
            )
            .order_by(Message.created_at.asc())
            .all()
        )