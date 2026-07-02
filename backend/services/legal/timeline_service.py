import re


class TimelineService:

    @staticmethod
    def extract(
        text: str
    ):

        dates = re.findall(
            r"\d{2}[/-]\d{2}[/-]\d{4}",
            text
        )

        return {
            "timeline": sorted(
                list(
                    set(dates)
                )
            )
        }