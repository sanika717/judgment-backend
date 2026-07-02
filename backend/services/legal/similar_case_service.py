from vector_store.chroma_store import (
    ChromaStore
)


class SimilarCaseService:

    @staticmethod
    def find(
        query: str,
        document_id: int
    ):

        vector_db = (
            ChromaStore.load(
                document_id
            )
        )

        results = (
            vector_db.similarity_search(
                query,
                k=5
            )
        )

        return [
            doc.page_content
            for doc in results
        ]