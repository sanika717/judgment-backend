from models.chat import Chat

from repositories.chat_repository import (
    ChatRepository
)


class SessionService:

    @staticmethod
    def create_session(
        db,
        user_id,
        title,
        document_id=None
    ):

        session = Chat(
            user_id=user_id,
            title=title,
            document_id=document_id
        )

        return ChatRepository.create(
            db,
            session
        )