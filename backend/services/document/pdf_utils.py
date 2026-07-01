from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
import os

COLOR_MAP = {
    "JUDGE": colors.HexColor("#6a5acd"),
    "APPELLANT": colors.HexColor("#0b8457"),
    "RESPONDENT": colors.HexColor("#d9534f"),
    "OTHER": colors.black,
}

def generate_bilingual_pdf(doc_id: str, paragraphs: list, translated_paragraphs: list = None, out_dir="/tmp"):
    out_path = os.path.join(out_dir, f"{doc_id}_bilingual.pdf")
    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4
    y = height - 2*cm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2*cm, y, f"Document: {doc_id}")
    y -= 1*cm
    c.setFont("Helvetica", 10)

    for idx, p in enumerate(paragraphs):
        role = p.get("role", "OTHER")
        text = p.get("text", "")[:1000]
        c.setFillColor(COLOR_MAP.get(role, colors.black))
        wrapped = text.replace("\n", " ")
        c.drawString(2*cm, y, wrapped[:200])
        if translated_paragraphs and idx < len(translated_paragraphs):
            c.setFillColor(colors.black)
            c.drawString(width/2 + 1*cm, y, translated_paragraphs[idx][:200])
        y -= 1*cm
        if y < 3*cm:
            c.showPage()
            y = height - 2*cm
            c.setFont("Helvetica", 10)
    c.save()
    return out_path
