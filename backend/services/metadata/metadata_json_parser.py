import json


class MetadataJsonParser:

    @staticmethod
    def parse(text):

        try:

            return json.loads(
                text
            )

        except Exception:

            return {}
