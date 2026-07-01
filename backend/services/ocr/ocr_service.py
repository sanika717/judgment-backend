import easyocr


class OCRService:

    reader = easyocr.Reader(
        ["en"],
        gpu=False
    )

    @staticmethod
    def extract_text_from_image(
        image_path
    ):

        result = OCRService.reader.readtext(
            image_path,
            detail=0
        )

        return "\n".join(result)