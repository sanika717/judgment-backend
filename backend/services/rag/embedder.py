from langchain_ollama import (
    OllamaEmbeddings
)

from config.settings import settings


class Embedder:

    @staticmethod
    def get_model():

        return OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL
        )