from sqlalchemy.orm import Session

from models.metadata import Metadata


class MetadataRepository:

    @staticmethod
    def create(
        db: Session,
        metadata: Metadata
    ):
        db.add(metadata)
        db.commit()
        db.refresh(metadata)

        return metadata