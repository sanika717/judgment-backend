from models.message import Message

from repositories.message_repository import (
    MessageRepository
)


class HistoryService:

    @staticmethod
    def save_user_message(
        db,
        session_id,
        content
    ):

        message = Message(
            session_id=session_id,
            sender="user",
            content=content
        )

        return MessageRepository.create(
            db,
            message
        )

    @staticmethod
    def save_ai_message(
        db,
        session_id,
        content
    ):

        message = Message(
            session_id=session_id,
            sender="assistant",
            content=content
        )

        return MessageRepository.create(
            db,
            message
        )

    @staticmethod
    def get_formatted_history(
        db,
        session_id
    ):

        messages = (
            MessageRepository
            .get_session_messages(
                db,
                session_id
            )
        )

        history = []

        for msg in messages:

            history.append(
                f"{msg.sender}: {msg.content}"
            )

        return "\n".join(history)