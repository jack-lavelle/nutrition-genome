from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter


def generate_pdf():
    # Create a new PDF file
    output_pdf = "output.pdf"
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Set font styles and sizes
    c.setFont("Helvetica-Bold", 16)  # Bold font, size 16
    c.setFont("Helvetica-Oblique", 12)  # Italic font, size 12
    c.setFont("Helvetica", 12)  # Regular font, size 12

    # Write the text
    c.drawString(100, 750, "OWM Nutrition Genome")  # Bold text
    c.setFont("Helvetica-Oblique", 12)  # Change font to italic
    c.drawString(100, 730, "Brain Health")  # Italic text
    c.setFont("Helvetica", 12)  # Change font to regular
    c.drawString(100, 700, get_lorem_ipsum())  # Regular text (Lorem Ipsum)

    c.showPage()  # Move to the next page
    c.save()  # Save the PDF

    # Merge the generated PDF with an empty one to remove the extra blank page
    merge_pdf_files(output_pdf, "empty.pdf", "final_output.pdf")
    print("PDF generated successfully!")


def merge_pdf_files(file1, file2, output_file):
    pdf_writer = PdfWriter()
    pdf_writer.add_blank_page(0, letter)
    with open(file1, "rb") as file1_obj, open(file2, "rb") as file2_obj:
        pdf_writer._add_object(file1_obj)
        pdf_writer._add_object(file2_obj)

    with open(output_file, "wb") as output_pdf:
        pdf_writer.write(output_pdf)


def get_lorem_ipsum():
    # Replace this with your own paragraph or desired text
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."


if __name__ == "__main__":
    generate_pdf()
