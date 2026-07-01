import os

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File
)

from sqlalchemy.orm import Session

from database.session import get_db

from api.dependencies import (
    get_current_user
)

from config.settings import settings

from services.document.document_upload_service import (
    DocumentUploadService
)

router = APIRouter()


@router.post("/")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    os.makedirs(
        settings.UPLOAD_DIR,
        exist_ok=True
    )

    filepath = os.path.join(
        settings.UPLOAD_DIR,
        file.filename
    )

    with open(
        filepath,
        "wb"
    ) as f:

        f.write(
            await file.read()
        )

    result = (
        DocumentUploadService.upload(
            db=db,
            title=file.filename,
            filename=file.filename,
            filepath=filepath,
            user_id=user.id
        )
    )

    return {
    "success": True,
    "document_id": (
        result["document"].id
    ),
    "metadata": (
        result["metadata"]
    ),
    "message":
        "Document processed successfully"
}