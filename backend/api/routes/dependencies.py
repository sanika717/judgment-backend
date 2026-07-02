from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from database.session import get_db

from core.security import verify_token

from repositories.user_repository import (
    UserRepository
)


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    print("TOKEN:", token)

    payload = verify_token(token)

    print("PAYLOAD:", payload)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    email = payload.get("sub")

    print("EMAIL:", email)

    user = UserRepository.get_by_email(
        db,
        email
    )

    print("USER:", user)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user