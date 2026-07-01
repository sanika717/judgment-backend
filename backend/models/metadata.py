from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from database.connection import Base


class Metadata(Base):

    __tablename__ = "metadata"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    court = Column(
        String(255)
    )

    judge = Column(
        String(255)
    )

    petitioner = Column(
        String(255)
    )

    respondent = Column(
        String(255)
    )

    case_number = Column(
        String(255)
    )

    citation = Column(
        String(255)
    )

    date = Column(
        String(255)
    )

    sections = Column(
        String(500)
    )