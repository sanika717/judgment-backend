from datetime import datetime

from sqlalchemy.orm import Session

from models.otp import OTPVerification


class OTPRepository:

    @staticmethod
    def create(
        db: Session,
        otp_record: OTPVerification
    ):
        db.add(otp_record)
        db.commit()
        db.refresh(otp_record)

        return otp_record

    @staticmethod
    def get_valid_otp(
        db: Session,
        email: str,
        otp: str
    ):
        return (
            db.query(OTPVerification)
            .filter(
                OTPVerification.email == email,
                OTPVerification.otp == otp,
                OTPVerification.is_used == False,
                OTPVerification.expires_at > datetime.utcnow()
            )
            .first()
        )