from sqlalchemy.orm import Session

from models.document import Document


class DocumentRepository:

    @staticmethod
    def create(
        db: Session,
        document: Document
    ):
        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def get_by_id(
        db: Session,
        document_id: int
    ):
        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(
            Document
        ).all()