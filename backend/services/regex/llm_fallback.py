from services.llm.factory import (
    LLMFactory
)


class LLMFallback:

    @staticmethod
    def complete_metadata(
        text: str,
        metadata: dict
    ):

        missing_fields = [
            key
            for key, value in metadata.items()
            if not value
        ]

        if not missing_fields:
            return metadata

        llm = LLMFactory.create()

        prompt = f"""
You are an expert legal metadata extractor.

Missing fields:
{missing_fields}

Extract ONLY those fields from the judgment.

Return valid JSON only.

TEXT:

{text[:6000]}
"""

        response = llm.invoke(prompt)

        metadata["llm_extracted"] = (
            response.content
        )

        return metadata