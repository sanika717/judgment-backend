class DashboardService:

    @staticmethod
    def get_dashboard(
        db,
        user_id
    ):

        documents = (
            DocumentRepository
            .count_user_documents(
                db,
                user_id
            )
        )

        sessions = (
            ChatSessionRepository
            .count_user_sessions(
                db,
                user_id
            )
        )

        return {
            "documents": documents,
            "sessions": sessions
        }