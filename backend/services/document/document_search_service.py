from repositories.document_repository import (
    DocumentRepository
)


class DocumentSearchService:

    @staticmethod
    def list_documents(
        db
    ):

        return (
            DocumentRepository.get_all(
                db
            )
        )

    @staticmethod
    def get_document(
        db,
        document_id
    ):

        return (
            DocumentRepository.get_by_id(
                db,
                document_id
            )
        )