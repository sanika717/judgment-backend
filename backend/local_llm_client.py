import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

# Local LLM (for answering queries)
llm = Ollama(model=OLLAMA_MODEL)

# Local Embeddings (for Chroma DB)
embedding_fn = OllamaEmbeddings(model=OLLAMA_EMBED_MODEL)

def generate_text(prompt: str) -> str:
    """Generate text using local Ollama model."""
    return llm.invoke(prompt)

def get_embedding(text: str):
    """Return vector embedding for text using Ollama."""
    return embedding_fn.embed_query(text)
