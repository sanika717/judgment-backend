from repositories.document_repository import (
    DocumentRepository
)

from services.translation.translation_service import (
    TranslationService
)

from services.document.document_service import (
    DocumentService
)


class DocumentTranslationService:

    @staticmethod
    def translate_document(
        db,
        document_id,
        language
    ):

        document = (
            DocumentRepository
            .get_by_id(
                db,
                document_id
            )
        )

        text = (
            DocumentService.process_document(
                document.file_path
            )
        )

        return (
            TranslationService.translate(
                text,
                language
            )
        )