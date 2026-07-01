from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.session import get_db

from services.metadata.metadata_search_service import (
    MetadataSearchService
)

router = APIRouter()


@router.get("/judge")
def search_judge(
    judge: str,
    db: Session = Depends(get_db)
):

    results = (
        MetadataSearchService
        .search_by_judge(
            db,
            judge
        )
    )

    return {
        "success": True,
        "data": results
    }


@router.get("/court")
def search_court(
    court: str,
    db: Session = Depends(get_db)
):

    results = (
        MetadataSearchService
        .search_by_court(
            db,
            court
        )
    )

    return {
        "success": True,
        "data": results
    }
