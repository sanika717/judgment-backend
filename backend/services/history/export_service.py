from reportlab.pdfgen import canvas


class PDFExportService:

    @staticmethod
    def export_chat(
        messages,
        output_path
    ):

        pdf = canvas.Canvas(
            output_path
        )

        y = 800

        for msg in messages:

            pdf.drawString(
                40,
                y,
                f"{msg.sender}: "
                f"{msg.content[:100]}"
            )

            y -= 20

        pdf.save()

        return output_path
