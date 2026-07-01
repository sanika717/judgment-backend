from langchain_chroma import Chroma

from config.settings import settings

from services.rag.embedder import (
    Embedder
)

from vector_store.collection_manager import (
    CollectionManager
)


class ChromaStore:

    @staticmethod
    def create(
        document_id: int,
        chunks
    ):

        collection_name = (
            CollectionManager
            .get_collection_name(
                document_id
            )
        )

        embeddings = (
            Embedder.get_model()
        )

        db = Chroma.from_texts(
            texts=chunks,
            embedding=embeddings,
            persist_directory=settings.CHROMA_PATH,
            collection_name=collection_name
        )

        return db

    @staticmethod
    def load(
        document_id: int
    ):

        collection_name = (
            CollectionManager
            .get_collection_name(
                document_id
            )
        )

        return Chroma(
            persist_directory=settings.CHROMA_PATH,
            collection_name=collection_name,
            embedding_function=Embedder.get_model()
        )