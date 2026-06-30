from src.local_client import generate_text

def translate_text(text: str, target_lang: str = "hi", model="llama3"):
    prompt = f"Translate the following legal text to {target_lang}. Keep legal terms intact and preserve paragraph alignment.\n\nText:\n{text[:20000]}"
    return generate_text(prompt, model=model)
