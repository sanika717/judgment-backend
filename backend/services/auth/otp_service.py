import random

from datetime import (
    datetime,
    timedelta
)

from models.otp import OTPVerification


class OTPService:

    @staticmethod
    def generate():

        return str(
            random.randint(
                100000,
                999999
            )
        )

    @staticmethod
    def send_otp(
        db,
        email: str
    ):

        otp = OTPService.generate()

        otp_record = OTPVerification(
            email=email,
            otp=otp,
            is_used=False,
            expires_at=datetime.utcnow() + timedelta(minutes=10)
        )

        db.add(otp_record)
        db.commit()

        print(f"EMAIL: {email}")
        print(f"OTP: {otp}")

        return True

    @staticmethod
    def verify_otp(
        db,
        email: str,
        otp: str
    ):

        otp_record = (
            db.query(OTPVerification)
            .filter(
                OTPVerification.email == email,
                OTPVerification.otp == otp,
                OTPVerification.is_used == False
            )
            .first()
        )

        if not otp_record:
            return False

        if otp_record.expires_at < datetime.utcnow():
            return False

        otp_record.is_used = True

        db.commit()

        return True