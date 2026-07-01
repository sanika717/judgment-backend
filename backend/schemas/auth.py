from pydantic import (
    BaseModel,
    EmailStr,
    ConfigDict
)


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    remember_device: bool = False


class VerifyOTPRequest(BaseModel):
    email: EmailStr
    otp: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

    model_config = ConfigDict(
        from_attributes=True
    )


class AuthResponse(BaseModel):
    success: bool
    message: str
