from fastapi import APIRouter

from api.routes.auth import router as auth_router
from api.routes.upload import router as upload_router
from api.routes.chat import router as chat_router
from api.routes.history import router as history_router
from api.routes.documents import router as documents_router
from api.routes.users import router as users_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(upload_router, prefix="/upload", tags=["upload"])
router.include_router(chat_router, prefix="/chat", tags=["chat"])
router.include_router(history_router, prefix="/history", tags=["history"])
router.include_router(documents_router, prefix="/documents", tags=["documents"])
router.include_router(users_router, prefix="/users", tags=["users"])
