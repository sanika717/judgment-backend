from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.session import get_db

from models.metadata import Metadata

router = APIRouter()


@router.get("/{document_id}")
def get_metadata(
    document_id: int,
    db: Session = Depends(get_db)
):

    metadata = (
        db.query(Metadata)
        .filter(
            Metadata.document_id
            == document_id
        )
        .first()
    )

    return {
        "success": True,
        "data": metadata
    }