from fastapi import APIRouter

from services.legal.similar_case_service import (
    SimilarCaseService
)

router = APIRouter()


@router.post("/")
def similar_cases(
    data: dict
):

    return {
        "results":
        SimilarCaseService.find(
            query=data["query"],
            document_id=data["document_id"]
        )
    }