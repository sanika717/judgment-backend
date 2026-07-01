from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.session import get_db

from services.document.document_search_service import (
    DocumentSearchService
)

router = APIRouter()


@router.get("/")
def list_documents(
    db: Session = Depends(get_db)
):

    documents = (
        DocumentSearchService
        .list_documents(db)
    )

    return {
        "success": True,
        "count": len(documents),
        "data": documents
    }


@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db)
):

    document = (
        DocumentSearchService
        .get_document(
            db,
            document_id
        )
    )
@router.delete(
    "/{document_id}"
)
def delete_document(
    document_id: int,
    db: Session = Depends(get_db)
):

    document = (
        DocumentRepository
        .get_by_id(
            db,
            document_id
        )
    )

    if not document:

        return {
            "success": False,
            "message":
            "Document not found"
        }

    DocumentDeleteService.delete(
        db,
        document
    )

    return {
        "success": True
    }
    return {
        "success": True,
        "data": document
    }