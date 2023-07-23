from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Image,
    ListItem,
    ListFlowable,
)
from Section import Section
from Person import Person
from Utilities import Utilities
from reportlab.lib.colors import CMYKColor


styles = getSampleStyleSheet()
styles["Title"].alignment = 0

selected_styles = {
    "Title": styles["Title"],
    "SectionTitle": styles["SectionTitle"],
    "Significance": styles["Significance"],
    "Normal": styles["Normal"],
}


def create_pdf(person: Person):
    # Create a new PDF file
    output_pdf = "output.pdf"
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)

    # Define the content
    content = []
    content.append(Paragraph("Nutrition Genome", styles["Title"]))
    content.append(Paragraph(person.name, styles["SectionTitle"]))

    for section_title in list(Utilities.get_gene_master_data().keys()):
        add_section(content, Section(section_title, genes=None))

    # Add the image at the top-center of the first page
    image_path = "owm_resources/logo.png"  # Replace with the path to your PNG file
    image = Image(image_path)
    image.drawHeight = 100  # Adjust the image height as needed
    image.drawWidth = 100  # Scale the image while maintaining aspect ratio
    image.hAlign = "CENTER"  # Center-align the image
    image.spaceAfter = 20  # Add space after the image
    content.insert(0, image)

    # Build the PDF document
    doc.build(content)
    print("PDF generated successfully!")


def create_bullet_pdf():
    doc = SimpleDocTemplate("output.pdf", pagesize=letter)
    bullet_style = styles["Normal"]
    bullet_style.spaceBefore = 10

    bullet_list = ["Bullet1", "Bullet2", "Bullet3", "Bullet4"]

    l = []

    for bullet in bullet_list:
        l.append(
            ListItem(
                Paragraph(bullet),
                bulletColor=CMYKColor(0, 0, 0, 1),
            )
        )

    list_flowable = ListFlowable(
        l,
        bulletType="bullet",
        bulletColor="black",
        bulletFontName="Times",
        bulletFontSize=12,
        bulletOffsetY=1,
        spaceBefore=5,
        spaceAfter=5,
        leftIndent=7,
    )

    story = []
    story.append(list_flowable)

    doc.build(story)
    print("PDF generated successfully!")


def add_section(content: list, section: Section):
    content.append(Paragraph(section.section_title, styles["SectionTitle"]))
    print(section.genes)
    for gene in section.genes:
        content.append(
            Paragraph(
                section.content[gene]["Significance"] + ".", styles["Significance"]
            )
        )
        add_body(content, section, gene)


def add_body(content, section, gene):
    gene_content_dict = section.content[gene]["Include"]
    for category in gene_content_dict:
        if not section.content[gene]["Include"][category]:
            pass
        bullet_list = section.content[gene]["Include"][category]
        add_bullet_list_to_content(content, bullet_list)


def add_bullet_list_to_content(content, bullet_list):
    for bullet in bullet_list:
        l = []
        l.append(ListItem(Paragraph(bullet), bulletColor=CMYKColor(0, 0, 0, 1)))

        list_flowable = ListFlowable(
            l,
            bulletType="bullet",
            bulletColor="black",
            bulletFontName="Helvetica",
            bulletFontSize=12,
            bulletOffsetY=1,
            spaceBefore=5,
            spaceAfter=5,
            leftIndent=7,
        )

        content.append(list_flowable)


def createSection():
    sectionHeader = Paragraph("<u><i>Brain Health</i></u>", styles["SectionTitle"])

    return sectionHeader


def createSubSection():
    significance = Paragraph(
        "Lower cannabinoid levels: Higher anxiety and stress perception. Less 'blissful'",
        styles["Significance"],
    )
    lifestyle_list = [
        "Running and biking > 30 minutes",
        "Strenuous hiking at high altitude",
        "Meditation, Yoga and deep breathing",
    ]
    nutrition_list = [
        "Red clover tea (women)",
        "Kaempfero: green leafy vegetables, including spinach and kale, and herbs such as dill, chives, and tarragon",
        "Cacao",
        "Genistein: Soy milk, soy flour, soy protein isolates, textured soy protein, Tempe",
        "Echinacea tea",
        "7-hydroxyflavone (parsley, onions, berries, tea, and citrus fruits)",
        "Beta-caryophyllene (cloves, rosemary, hops)",
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
    create_pdf(Person("Jack LaVelle"))
    # create_bullet_pdf()
