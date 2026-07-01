from models.metadata import Metadata


class MetadataSearchService:

    @staticmethod
    def search_by_judge(
        db,
        judge
    ):

        return (
            db.query(Metadata)
            .filter(
                Metadata.judge.ilike(
                    f"%{judge}%"
                )
            )
            .all()
        )

    @staticmethod
    def search_by_court(
        db,
        court
    ):

        return (
            db.query(Metadata)
            .filter(
                Metadata.court.ilike(
                    f"%{court}%"
                )
            )
            .all()
        )