class VectorRegistry:
    """
    Stores document-specific retrievers in memory.

    Upload PDF
        ↓
    Create Retriever
        ↓
    Register Retriever
        ↓
    Chat API retrieves it later
    """

    _retrievers = {}

    @classmethod
    def register(
        cls,
        document_id: int,
        retriever
    ):
        cls._retrievers[
            document_id
        ] = retriever

    @classmethod
    def get(
        cls,
        document_id: int
    ):
        return cls._retrievers.get(
            document_id
        )

    @classmethod
    def exists(
        cls,
        document_id: int
    ) -> bool:
        return (
            document_id
            in cls._retrievers
        )

    @classmethod
    def remove(
        cls,
        document_id: int
    ):
        if document_id in cls._retrievers:
            del cls._retrievers[
                document_id
            ]

    @classmethod
    def clear(cls):
        cls._retrievers.clear()

    @classmethod
    def list_documents(cls):
        return list(
            cls._retrievers.keys()
        )