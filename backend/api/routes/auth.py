from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from api.dependencies import get_current_user
from fastapi import Depends
from database.session import get_db

from schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from services.auth.auth_service import AuthService


router = APIRouter()


@router.post("/register")
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db)
):

    try:

        result = AuthService.register(
            db=db,
            username=payload.username,
            email=payload.email,
            password=payload.password
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login")
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):

    try:

        return AuthService.login(
            db=db,
            email=payload.email,
            password=payload.password
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )


@router.get("/test")
def auth_test():

    return {
        "success": True,
        "message": "Auth route working"
    }
@router.get("/me")
def profile(
    user=Depends(get_current_user)
):

    return {
        "success": True,
        "data": {
            "username": user.username,
            "email": user.email
        }
    }