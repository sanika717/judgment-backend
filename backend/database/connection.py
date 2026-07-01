from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from config.settings import settings

if settings.DATABASE_URL.startswith("sqlite"):

    engine = create_engine(
        settings.DATABASE_URL,
        connect_args={
            "check_same_thread": False
        }
    )

else:

    engine = create_engine(
        settings.DATABASE_URL
    )

Base = declarative_base()