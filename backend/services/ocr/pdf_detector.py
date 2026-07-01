import fitz


class PDFDetector:

    @staticmethod
    def is_scanned_pdf(pdf_path: str):

        document = fitz.open(pdf_path)

        page = document[0]

        text = page.get_text()

        document.close()

        return len(text.strip()) < 50