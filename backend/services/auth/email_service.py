import logging

logger = logging.getLogger(__name__)


class EmailService:

    @staticmethod
    def send_otp(
        email: str,
        otp: str
    ):
        logger.info(
            f"OTP for {email}: {otp}"
        )

        print(
            f"\n📧 OTP SENT TO {email}: {otp}\n"
        )

        return True
