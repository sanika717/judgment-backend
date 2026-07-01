from repositories.document_repository import (
    DocumentRepository
)

from services.speech.tts_service import (
    TTSService
)

from services.document.document_service import (
    DocumentService
)


class DocumentAudioService:

    @staticmethod
    def generate_audio(
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

        text = (
            DocumentService.process_document(
                document.file_path
            )
        )

        return (
            TTSService.generate_audio(
                text=text[:5000],
                filename=f"doc_{document_id}"
            )
        )