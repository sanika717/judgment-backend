from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from database.connection import Base


class TrustedDevice(Base):

    __tablename__ = "trusted_devices"

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

    device_token = Column(
        String(255),
        unique=True,
        nullable=False
    )

    user_agent = Column(
        String(500)
    )

    last_login = Column(
        DateTime,
        default=datetime.utcnow
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )