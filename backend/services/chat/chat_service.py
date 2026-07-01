from vector_store.retriever_service import (
    RetrieverService
)

from services.rag.rag_service import (
    RAGService
)

from services.history.history_service import (
    HistoryService
)


class ChatService:

    @staticmethod
    def ask(
        db,
        document_id: int,
        session_id: int,
        question: str,
        language: str = "English"
    ):

        retriever = (
    RetrieverService.get_retriever(
        document_id
    )
)

        history = (
            HistoryService
            .get_formatted_history(
                db,
                session_id
            )
        )

        HistoryService.save_user_message(
            db,
            session_id,
            question
        )

        answer = (
            RAGService.ask_question(
                retriever=retriever,
                question=question,
                history=history,
                language=language
            )
        )

        HistoryService.save_ai_message(
            db,
            session_id,
            answer
        )

        return answer