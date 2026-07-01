import re


class MetadataExtractor:

    @staticmethod
    def extract(text):

        metadata = {
            "court": None,
            "judge": None,
            "petitioner": None,
            "respondent": None,
            "case_number": None,
            "citation": None,
            "date": None,
            "sections": []
        }

        court = re.search(
            r"IN THE (.+?COURT.*?)\n",
            text,
            re.IGNORECASE
        )

        if court:
            metadata["court"] = (
                court.group(1).strip()
            )

        judge = re.search(
            r"Justice\s+([A-Za-z\s.]+)",
            text
        )

        if judge:
            metadata["judge"] = (
                judge.group(1).strip()
            )

        sections = re.findall(
            r"Section\s+(\d+)",
            text,
            re.IGNORECASE
        )

        if sections:
            metadata["sections"] = (
                list(set(sections))
            )

        return metadata