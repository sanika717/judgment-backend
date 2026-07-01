from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text
)

from database.connection import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    original_filename = Column(
        String(255),
        nullable=False
    )

    file_path = Column(
        String(500),
        nullable=False
    )

    document_type = Column(
        String(50),
        default="judgement"
    )

    language = Column(
        String(50),
        default="English"
    )

    summary = Column(
        Text,
        nullable=True
    )

    upload_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    processed_at = Column(
        DateTime,
        nullable=True
    )

    status = Column(
        String(50),
        default="uploaded"
    )