class CollectionManager:

    @staticmethod
    def get_collection_name(
        document_id: int
    ):

        return (
            f"document_{document_id}"
        )
