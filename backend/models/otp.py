from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from database.connection import Base


class OTPVerification(Base):

    __tablename__ = "otp_verifications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String(255),
        nullable=False
    )

    otp = Column(
        String(6),
        nullable=False
    )

    is_used = Column(
        Boolean,
        default=False
    )

    expires_at = Column(
        DateTime,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )