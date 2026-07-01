from models.document import Document

from repositories.document_repository import (
    DocumentRepository
)

from services.document.document_ingestion_service import (
    DocumentIngestionService
)

from services.document.document_metadata_service import (
    DocumentMetadataService
)


class DocumentUploadService:

    @staticmethod
    def upload(
        db,
        title,
        filename,
        filepath,
        user_id
    ):

        document = Document(
            title=title,
            original_filename=filename,
            file_path=filepath,
            user_id=user_id
        )

        document = DocumentRepository.create(
            db,
            document
        )

        result = (
            DocumentIngestionService.ingest(
                pdf_path=filepath,
                document_id=document.id
            )
        )

        DocumentMetadataService.save_metadata(
            db=db,
            document_id=document.id,
            extracted_metadata=result["metadata"]
        )

        return {
            "document": document,
            "metadata": result["metadata"]
        }
