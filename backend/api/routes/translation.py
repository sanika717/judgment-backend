from fastapi import APIRouter
from pydantic import BaseModel

from services.translation.translation_service import (
    TranslationService
)

router = APIRouter()


class TranslationRequest(BaseModel):

    text: str
    target_language: str


@router.post("/")
def translate(
    payload: TranslationRequest
):

    translated = (
        TranslationService.translate(
            payload.text,
            payload.target_language
        )
    )

    return {
        "success": True,
        "data": {
            "translated_text": translated
        }
    }