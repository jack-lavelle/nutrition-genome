from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from Section import Section


def generate_pdf():
    # Create a new PDF file
    output_pdf = "output.pdf"
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)

    # Define paragraph styles
    styles = getSampleStyleSheet()
    bold_style = styles["Title"]
    bold_style.alignment = 0
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
    content.append(Paragraph("Nutrition Genome", bold_style))
    content.extend([createSection(), createSubSection()])
    content.append(Paragraph(get_lorem_ipsum(), regular_style))
    
    # Add the image at the top-center of the first page
    image_path = "logo.png"  # Replace with the path to your PNG file
    image = Image(image_path)
    image.drawHeight = 100 # Adjust the image height as needed
    image.drawWidth = 100   # Scale the image while maintaining aspect ratio
    image.hAlign = "CENTER"  # Center-align the image
    image.spaceAfter = 20  # Add space after the image
    content.insert(0, image)

    # Build the PDF document
    doc.build(content)
    print("PDF generated successfully!")

def createSection():
    styles = getSampleStyleSheet()
    section_title_style = styles["SectionTitle"]
    sectionHeader = Paragraph("<u><i>Brain Health</i></u>", section_title_style)
    
    return sectionHeader

def createSubSection():
    styles = getSampleStyleSheet()
    significance_style = styles["Significance"]
    significance = Paragraph("Lower cannabinoid levels: Higher anxiety and stress perception. Less 'blissful'", significance_style)
    lifestyle_list = [
          "Running and biking > 30 minutes",
          "Strenuous hiking at high altitude",
          "Meditation, Yoga and deep breathing"
    ]
    nutrition_list = [
          "Red clover tea (women)",
          "Kaempfero: green leafy vegetables, including spinach and kale, and herbs such as dill, chives, and tarragon",
          "Cacao",
          "Genistein: Soy milk, soy flour, soy protein isolates, textured soy protein, Tempe",
          "Echinacea tea",
          "7-hydroxyflavone (parsley, onions, berries, tea, and citrus fruits)",
          "Beta-caryophyllene (cloves, rosemary, hops)"
    ]
    avoid_list = ["Pesticides", "CBD oil", "Phthalates"]
    
    lifestyle = Paragraph(lifestyle_list[0], styles["Bullet"])
    subSection = []
    subSection.extend([significance, lifestyle])
    
    return subSection
    
    

def get_lorem_ipsum():
    # Replace this with your own paragraph or desired text
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."


if __name__ == "__main__":
    generate_pdf()
