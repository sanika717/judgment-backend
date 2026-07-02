from reportlab.pdfgen import canvas


class ExportPdfService:

    @staticmethod
    def export(
        messages,
        output_file
    ):

        pdf = canvas.Canvas(
            output_file
        )

        y = 800

        for msg in messages:

            pdf.drawString(
                50,
                y,
                msg.content
            )

            y -= 20

        pdf.save()

        return output_file