from services.llm.factory import (
    LLMFactory
)


class SummarizerService:

    @staticmethod
    def summarize(text: str):

        llm = LLMFactory.create()

        prompt = f"""
Summarize the following legal judgment.

TEXT:

{text[:10000]}
"""

        response = llm.invoke(prompt)

        return response.content