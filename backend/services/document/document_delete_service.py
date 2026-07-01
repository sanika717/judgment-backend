import os

from repositories.document_repository import (
    DocumentRepository
)


class DocumentDeleteService:

    @staticmethod
    def delete(
        db,
        document
    ):

        if (
            document.file_path
            and
            os.path.exists(
                document.file_path
            )
        ):

            os.remove(
                document.file_path
            )

        db.delete(document)

        db.commit()
