from fastapi import APIRouter

from services.legal.timeline_service import (
    TimelineService
)

router = APIRouter()


@router.post("/")
def timeline(
    data: dict
):

    return (
        TimelineService.extract(
            data["text"]
        )
    )