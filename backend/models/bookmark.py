from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
)

from database.connection import Base


class Bookmark(Base):

    __tablename__ = "bookmarks"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    question = Column(Text)

    answer = Column(Text)