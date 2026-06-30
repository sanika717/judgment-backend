from langchain_ollama import ChatOllama

def generate_text(prompt: str, model: str = "llama3", max_output_tokens: int = 1024) -> str:
    llm = ChatOllama(model=model, temperature=0)
    resp = llm.invoke(prompt)
    return resp.content if hasattr(resp, "content") else str(resp)
