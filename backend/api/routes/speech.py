from fastapi import APIRouter
from pydantic import BaseModel

from services.speech.tts_service import (
    TTSService
)

router = APIRouter()


class SpeechRequest(BaseModel):

    text: str
    filename: str


@router.post("/")
def speech(
    payload: SpeechRequest
):

    path = (
        TTSService.generate_audio(
            payload.text,
            payload.filename
        )
    )

    return {
        "success": True,
        "data": {
            "audio_file": path
        }
    }