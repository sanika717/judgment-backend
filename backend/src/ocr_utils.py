import os, io
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from dotenv import load_dotenv
from config import OCR_MODE

load_dotenv()
POPPLER_PATH = os.getenv("POPPLER_PATH")  # for Windows

def _tesseract_image_to_text(pil_img: Image.Image, lang="eng"):
    return pytesseract.image_to_string(pil_img, lang=lang)

def ocr_pdf_to_pages(pdf_path: str, dpi: int = 300):
    """OCR using Tesseract (offline)"""
    images = convert_from_path(pdf_path, dpi=dpi, poppler_path=POPPLER_PATH)
    texts = []
    for img in images:
        texts.append(_tesseract_image_to_text(img))
    return texts
