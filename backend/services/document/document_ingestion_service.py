from services.document.document_service import (
    DocumentService
)

from services.regex.metadata_extractor import (
    MetadataExtractor
)

from services.rag.chunker import (
    Chunker
)

from services.rag.vector_registry import (
    VectorRegistry
)

from vector_store.chroma_store import (
    ChromaStore
)
from services.regex.llm_fallback import (
    LLMFallback
)
class DocumentIngestionService:

    @staticmethod
    def ingest(
        pdf_path: str,
        document_id: int
    ):

        text = DocumentService.process_document(
            pdf_path
        )

        metadata = MetadataExtractor.extract(
            text
        )
        metadata = (
            LLMFallback.complete_metadata(
            text,
            metadata
    )
)
        chunks = Chunker.create_chunks(
            text
        )

        vector_db = ChromaStore.create(
        document_id=document_id,
        chunks=chunks
        )

        retriever = vector_db.as_retriever(
            search_kwargs={"k": 5}
        )

        VectorRegistry.register(
            document_id=document_id,
            retriever=retriever
        )

        return {
            "text": text,
            "metadata": metadata,
            "chunks": len(chunks)
        }