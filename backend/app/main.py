from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings

from core.logging import setup_logging

from middleware.request_logger import (
    RequestLoggerMiddleware
)

from middleware.exception_handler import (
    register_exception_handlers
)

from api.routes.auth import (
    router as auth_router
)

from api.routes.users import (
    router as users_router
)

from api.routes.upload import (
    router as upload_router
)

from api.routes.chat import (
    router as chat_router
)

from api.routes.history import (
    router as history_router
)

from api.routes.documents import (
    router as documents_router
)

from api.routes.summary import (
    router as summary_router
)

from api.routes.translation import (
    router as translation_router
)

from api.routes.speech import (
    router as speech_router
)

from database.connection import (
    Base,
    engine
)
from api.routes.session import (
    router as session_router
)
from api.routes.analytics import (
    router as analytics_router
)

from api.routes.profile import (
    router as profile_router
)
from api.routes.search import (
    router as search_router
)
from api.routes.metadata import (
    router as metadata_router
)
from api.routes.document_ai import (
    router as document_ai_router
)
def create_app() -> FastAPI:

    setup_logging()

    Base.metadata.create_all(bind=engine)

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="AI Legal Judgement Assistant"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(
        session_router,
        prefix="/api/session",
        tags=["Sessions"]
    )
    
    app.include_router(
    analytics_router,
    prefix="/api/analytics",
    tags=["Analytics"]
    )

    app.include_router(
    analytics_router,
    prefix="/api/profile",
    tags=["Profile"]
    )

    app.include_router( 
    profile_router,
    prefix="/api/profile",
    tags=["Profile"]
    )
    
    app.include_router(
    search_router,
    prefix="/api/search",
    tags=["Metadata Search"]
    )

    app.include_router(
    document_ai_router,
    prefix="/api/document-ai",
    tags=["Document AI"]
    )
    app.add_middleware(
        RequestLoggerMiddleware
    )

    register_exception_handlers(app)

    # -------------------------
    # Authentication
    # -------------------------

    app.include_router(
        auth_router,
        prefix="/api/auth",
        tags=["Authentication"]
    )

    # -------------------------
    # Users
    # -------------------------

    app.include_router(
        users_router,
        prefix="/api/users",
        tags=["Users"]
    )

    # -------------------------
    # Documents
    # -------------------------

    app.include_router(
        upload_router,
        prefix="/api/upload",
        tags=["Upload"]
    )

    app.include_router(
        documents_router,
        prefix="/api/documents",
        tags=["Documents"]
    )

    # -------------------------
    # Chat
    # -------------------------

    app.include_router(
        chat_router,
        prefix="/api/chat",
        tags=["Chat"]
    )

    app.include_router(
        history_router,
        prefix="/api/history",
        tags=["History"]
    )

    # -------------------------
    # AI Features
    # -------------------------

    app.include_router(
        summary_router,
        prefix="/api/summary",
        tags=["Summary"]
    )

    app.include_router(
        translation_router,
        prefix="/api/translation",
        tags=["Translation"]
    )

    app.include_router(
        speech_router,
        prefix="/api/speech",
        tags=["Text To Speech"]
    )

    # -------------------------
    # Health Check
    # -------------------------

    @app.get("/", tags=["System"])
    async def root():

        return {
            "success": True,
            "message": "AI Legal Judgement Assistant Running",
            "version": settings.APP_VERSION
        }

    @app.get("/health", tags=["System"])
    async def health():

        return {
            "success": True,
            "status": "healthy",
            "services": {
                "database": "connected",
                "authentication": "enabled",
                "ocr": "enabled",
                "rag": "enabled",
                "translation": "enabled",
                "tts": "enabled"
            }
        }

    return app


app = create_app()