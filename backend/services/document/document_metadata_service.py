from models.metadata import Metadata

from repositories.metadata_repository import (
    MetadataRepository
)


class DocumentMetadataService:

    @staticmethod
    def save_metadata(
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
            petitioner=extracted_metadata.get(
                "petitioner"
            ),
            respondent=extracted_metadata.get(
                "respondent"
            ),
            case_number=extracted_metadata.get(
                "case_number"
            ),
            citation=extracted_metadata.get(
                "citation"
            ),
            date=extracted_metadata.get(
                "date"
            ),
            sections=str(
                extracted_metadata.get(
                    "sections",
                    []
                )
            )
        )

        return MetadataRepository.create(
            db,
            metadata
        )