from services.llm.ollama import (
    OllamaService
)

from config.settings import settings


class LLMFactory:

    @staticmethod
    def create():

        if (
            settings.LLM_PROVIDER
            == "ollama"
        ):
            return (
                OllamaService.get_llm()
            )

        raise ValueError(
            "Unsupported provider"
        )