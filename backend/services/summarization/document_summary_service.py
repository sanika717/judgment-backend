from repositories.document_repository import (
    DocumentRepository
)

from services.summarization.summarizer_service import (
    SummarizerService
)

from services.document.document_service import (
    DocumentService
)


class DocumentSummaryService:

    @staticmethod
    def generate(
        db,
        document_id
    ):

        document = (
            DocumentRepository
            .get_by_id(
                db,
                document_id
            )
        )

        if not document:
            raise ValueError(
                "Document not found"
            )

        text = (
            DocumentService.process_document(
                document.file_path
            )
        )

        return (
            SummarizerService
            .summarize(text)
        )