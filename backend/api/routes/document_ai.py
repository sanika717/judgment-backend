from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.session import get_db

from services.summarization.document_summary_service import (
    DocumentSummaryService
)

from services.translation.document_translation_service import (
    DocumentTranslationService
)

from services.speech.document_audio_service import (
    DocumentAudioService
)

router = APIRouter()


@router.get("/{document_id}/summary")
def summary(
    document_id: int,
    db: Session = Depends(get_db)
):

    result = (
        DocumentSummaryService.generate(
            db,
            document_id
        )
    )

    return {
        "success": True,
        "summary": result
    }


@router.get("/{document_id}/translate")
def translate(
    document_id: int,
    language: str,
    db: Session = Depends(get_db)
):

    result = (
        DocumentTranslationService
        .translate_document(
            db,
            document_id,
            language
        )
    )

    return {
        "success": True,
        "translated_text": result
    }


@router.get("/{document_id}/audio")
def audio(
    document_id: int,
    db: Session = Depends(get_db)
):

    path = (
        DocumentAudioService
        .generate_audio(
            db,
            document_id
        )
    )

    return {
        "success": True,
        "audio_file": path
    }
