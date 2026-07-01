class MetadataAnalyzer:

    @staticmethod
    def get_completion_score(
        metadata
    ):

        total = len(metadata)

        filled = len([
            value
            for value in metadata.values()
            if value
        ])

        return round(
            (filled / total) * 100,
            2
        )