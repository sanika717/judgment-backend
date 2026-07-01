import logging
import os

from config.settings import settings


def setup_logging():

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(settings.LOG_FILE),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger("legal-ai")