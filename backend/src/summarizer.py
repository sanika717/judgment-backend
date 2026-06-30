from src.local_client import generate_text

SHORT_PROMPT = """You are a legal assistant. Given the following passages, produce:
1) A 2-3 item short bullet summary (concise).
2) A detailed narrative summary (issues, arguments, ruling).
Return JSON: { "bullets": [...], "narrative": "..." }.
Passages:
{passages}
"""

def summarize_passages(passages: str, model="llama3"):
    prompt = SHORT_PROMPT.format(passages=passages[:25000])
    text = generate_text(prompt, model=model)
    return text
