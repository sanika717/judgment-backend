from models.metadata import Metadata

from repositories.metadata_repository import (
    MetadataRepository
)


class MetadataService:

    @staticmethod
    def save(
        db,
        document_id,
        extracted_metadata
    ):

        metadata = Metadata(
            document_id=document_id,
            court=extracted_metadata.get(
                "court"
            ),
            judge=extracted_metadata.get(
                "judge"
            ),
            case_number=extracted_metadata.get(
                "case_number"
            )
        )

        return MetadataRepository.create(
            db,
            metadata
        )
