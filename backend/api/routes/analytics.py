from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from api.dependencies import (
    get_current_user
)

from database.session import get_db

from services.analytics.analytics_service import (
    AnalyticsService
)

router = APIRouter()


@router.get("/")
def dashboard(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    data = (
        AnalyticsService.get_dashboard(
            db,
            user.id
        )
    )

    return {
        "success": True,
        "data": data
    }