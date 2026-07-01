try:
    from langchain_text_splitters import (
        RecursiveCharacterTextSplitter
    )
except ImportError:
    from langchain.text_splitter import (
        RecursiveCharacterTextSplitter
    )


class Chunker:

    @staticmethod
    def create_chunks(text: str):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=300
        )

        return splitter.split_text(text)