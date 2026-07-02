from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from repositories.document_repository import DocumentRepository

from services.document.document_delete_service import DocumentDeleteService


# This is what main.py is expecting
router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    repository = DocumentRepository(db)
    service = DocumentDeleteService(repository)

    result = service.execute(document_id)

    return {
        "success": True,
        "data": result
    }