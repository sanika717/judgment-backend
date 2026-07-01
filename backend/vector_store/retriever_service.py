from vector_store.chroma_store import (
    ChromaStore
)


class RetrieverService:

    @staticmethod
    def get_retriever(
        document_id: int
    ):

        vector_db = ChromaStore.load(
            document_id
        )

        return vector_db.as_retriever(
            search_kwargs={
                "k": 5
            }
        )