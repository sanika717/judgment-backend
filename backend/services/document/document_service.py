from services.document.pdf_processor import PDFProcessor
from services.document.text_cleaner import TextCleaner


class DocumentService:

    @staticmethod
    def process_document(pdf_path: str):

        raw_text = PDFProcessor.extract_text(
            pdf_path
        )

        cleaned_text = TextCleaner.clean(
            raw_text
        )

        return cleaned_text