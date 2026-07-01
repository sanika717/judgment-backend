from fastapi import APIRouter
from pydantic import BaseModel

from services.summarization.summarizer_service import (
    SummarizerService
)

router = APIRouter()


class SummaryRequest(BaseModel):
    text: str


@router.post("/")
def summarize(payload: SummaryRequest):

    summary = SummarizerService.summarize(
        payload.text
    )

    return {
        "success": True,
        "data": {
            "summary": summary
        }
    }