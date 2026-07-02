import json

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

        try:

            response = llm.invoke(prompt)

            result = json.loads(
                response.content
            )

            metadata.update(
                {
                    "court": result.get("court"),
                    "judge": result.get("judge"),
                    "petitioner": result.get("petitioner"),
                    "respondent": result.get("respondent"),
                    "case_number": result.get("case_number"),
                    "citation": result.get("citation"),
                    "date": result.get("date"),
                    "sections": result.get("sections", [])
                }
            )

        except Exception as e:

            print(
                "LLM metadata extraction error:",
                str(e)
            )

        return metadata