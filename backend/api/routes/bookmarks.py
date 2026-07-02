from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.session import get_db

from api.dependencies import (
    get_current_user
)

from models.bookmark import Bookmark

router = APIRouter()


@router.post("/")
def save_bookmark(
    data: dict,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    bookmark = Bookmark(
        user_id=current_user.id,
        question=data["question"],
        answer=data["answer"]
    )

    db.add(bookmark)

    db.commit()

    return {
        "success": True
    }


@router.get("/")
def get_bookmarks(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    bookmarks = (
        db.query(Bookmark)
        .filter(
            Bookmark.user_id
            ==
            current_user.id
        )
        .all()
    )

    return bookmarks