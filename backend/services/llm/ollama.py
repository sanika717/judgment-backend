from langchain_ollama import ChatOllama

from config.settings import settings


class OllamaService:

    @staticmethod
    def get_llm():

        return ChatOllama(
            model=settings.OLLAMA_MODEL,
            temperature=0
        )