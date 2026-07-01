from pdf2image import convert_from_path
import pytesseract
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

# Path to poppler and tesseract (update if installed elsewhere)
POPPLER_PATH = r"C:\\poppler-25.07.0\\Library\\bin"
TESSERACT_PATH = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# Convert PDF to images
pages = convert_from_path("testing ocr.pdf", poppler_path=POPPLER_PATH)

for i, page in enumerate(pages):
    try:
        text = pytesseract.image_to_string(page, lang="eng+hin")  # English + Hindi
        text = text.strip()
    except Exception as e:
        text = f"[ERROR] OCR failed for page {i+1}: {e}"

    print(f"--- Page {i+1} ---")
    print(text)
