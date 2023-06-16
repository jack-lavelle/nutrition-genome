from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph


def generate_pdf():
    # Create a new PDF file
    output_pdf = "output.pdf"
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)

    # Define paragraph styles
    styles = getSampleStyleSheet()
    bold_style = styles["Title"]
    italic_underline_style = ParagraphStyle(
        "italic_underline",
        parent=styles["Normal"],
        fontName="Times",
        fontSize=12,
        italic=True,
        underline=True,
    )
    regular_style = styles["Normal"]

    # Define the content
    content = []
    content.append(Paragraph("<b>OWM Nutrition Genome</b>", bold_style))
    content.append(Paragraph("<u><i>Brain Health</i></u>", italic_underline_style))
    content.append(Paragraph(get_lorem_ipsum(), regular_style))

    # Build the PDF document
    doc.build(content)
    print("PDF generated successfully!")


def get_lorem_ipsum():
    # Replace this with your own paragraph or desired text
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."


if __name__ == "__main__":
    generate_pdf()
