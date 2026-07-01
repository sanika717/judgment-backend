class HybridSearch:

    @staticmethod
    def search(
        vector_results,
        keyword_results
    ):

        combined = []

        combined.extend(
            vector_results
        )

        combined.extend(
            keyword_results
        )

        return combined