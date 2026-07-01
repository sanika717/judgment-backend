from models.user import User

from repositories.user_repository import UserRepository

from core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token
)

from services.auth.otp_service import OTPService


class AuthService:

    @staticmethod
    def register(
        db,
        username: str,
        email: str,
        password: str
    ):

        existing_user = UserRepository.get_by_email(
            db,
            email
        )

        if existing_user:
            raise ValueError(
                "Email already exists"
            )

        print("PASSWORD:", password)
        print("TYPE:", type(password))
        print("LENGTH:", len(password))

        password_hash = hash_password(password)

        user = User(
            username=username,
            email=email,
            password_hash=password_hash,
            is_verified=True
        )

        UserRepository.create(
            db,
            user
        )

        return {
            "success": True,
            "message": "User registered successfully"
        }

    @staticmethod
    def login(
        db,
        email: str,
        password: str
    ):

        user = UserRepository.get_by_email(
            db,
            email
        )

        if not user:
            raise ValueError(
                "Account not found"
            )

        if not verify_password(
            password,
            user.password_hash
        ):
            raise ValueError(
                "Invalid password"
            )

        access_token = create_access_token(
            {
                "sub": user.email
            }
        )

        refresh_token = create_refresh_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }