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
            .filter(
                Document.id == document_id
            )
            .first()
        )

    @staticmethod
    def get_all(
        db: Session
    ):
        return (
            db.query(Document)
            .all()
        )

    @staticmethod
    def get_user_documents(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Document)
            .filter(
                Document.user_id == user_id
            )
            .all()
        )

    @staticmethod
    def count_user_documents(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Document)
            .filter(
                Document.user_id == user_id
            )
            .count()
        )

    @staticmethod
    def delete(
        db: Session,
        document: Document
    ):
        db.delete(document)
        db.commit()