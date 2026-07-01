from repositories.document_repository import (
    DocumentRepository
)

from repositories.chat_repository import (
    ChatRepository
)


class AnalyticsService:

    @staticmethod
    def get_dashboard(
        db,
        user_id
    ):

        documents = (
            DocumentRepository
            .get_user_documents(
                db,
                user_id
            )
        )

        sessions = (
            ChatRepository
            .get_user_sessions(
                db,
                user_id
            )
        )

        return {
            "documents": len(documents),
            "sessions": len(sessions)
        }