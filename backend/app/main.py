import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings
from core.logging import configure_logging
from middleware.exception_handler import setup_exception_handlers
from middleware.request_logger import RequestLoggerMiddleware
from api.routes import router as api_router
from database.connection import engine, Base


def create_app() -> FastAPI:
    configure_logging()
    Base.metadata.create_all(bind=engine)

    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        description="AI Legal Judgement Assistant backend API",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(RequestLoggerMiddleware)
    setup_exception_handlers(app)
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.get("/health", tags=["health"])
    async def health_check():
        return {"success": True, "message": "Service is healthy", "data": {}}

    return app


app = create_app()
