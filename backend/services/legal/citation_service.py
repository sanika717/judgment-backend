import re


class CitationService:

    @staticmethod
    def extract(text):

        patterns = [

            r"\(\d{4}\)\s*\d+\s*SCC\s*\d+",

            r"AIR\s+\d{4}\s+\w+\s+\d+",

            r"\d{4}\s+SCC\s+OnLine\s+\w+\s+\d+"

        ]

        citations = []

        for p in patterns:

            citations.extend(
                re.findall(
                    p,
                    text
                )
            )

        return list(
            set(citations)
        )