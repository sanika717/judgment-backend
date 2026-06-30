from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import logging

logger = logging.getLogger("backend.request")

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Request {request.method} {request.url}")
        response = await call_next(request)
        logger.info(f"Response {response.status_code} for {request.url}")
        return response
