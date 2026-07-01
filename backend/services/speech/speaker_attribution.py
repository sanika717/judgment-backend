from backend.services.llm.local_client import generate_text
import json

PROMPT = """You are a legal assistant. Given the following paragraphs, label each paragraph as one of: JUDGE, APPELLANT, RESPONDENT, OTHER.
Return only valid JSON array: [{"id": 0, "role":"JUDGE","text":"..."}, ...]
Paragraphs:
{paras}
"""

def split_into_paragraphs(text):
    return [p.strip() for p in text.split("\n\n") if p.strip()]

def attribute_speakers(text: str, model="llama3"):
    paras = split_into_paragraphs(text)
    combined = "\n\n".join(paras[:200])
    resp = generate_text(PROMPT.format(paras=combined), model=model, max_output_tokens=2048)
    try:
        return json.loads(resp)
    except Exception:
        out = []
        for i, p in enumerate(paras):
            lp = p.lower()
            if "judgment" in lp or "held" in lp:
                role = "JUDGE"
            elif "appellant" in lp:
                role = "APPELLANT"
            elif "respondent" in lp:
                role = "RESPONDENT"
            else:
                role = "OTHER"
            out.append({"id": i, "role": role, "text": p})
        return out
