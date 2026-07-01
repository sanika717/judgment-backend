from services.llm.factory import (
    LLMFactory
)


class TranslationService:

    @staticmethod
    def translate(
        text,
        target_language
    ):

        llm = LLMFactory.create()

        prompt = f"""
Translate the following text to {target_language}.

TEXT:
{text}
"""

        response = llm.invoke(prompt)

        return response.content