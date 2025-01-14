import random
from Utilities import Utilities, load_master_data, generate_section_genes


class Section:
    gene_master_data = None
    section_title = None

    # a Section corresponds to the data from a number of genes from a single category
    def __init__(self, section_title, genes):
        # TODO: optional section_title
        self.section_title = section_title
        self.content = {}
        self.genes = genes

        self.set_content(self.genes)

    def set_content(self, genes: list):
        if not self.genes:
            self.genes = generate_section_genes(self.section_title)
        else:
            self.genes = genes

        for gene in self.genes:
            specific_gene_data = Utilities.gene_master_data[self.section_title][gene]
            self.content[gene] = {
                "Significance": specific_gene_data.get("Significance", ""),
                "Include": specific_gene_data.get("Include", ""),
                "Avoid": specific_gene_data.get("Avoid", ""),
            }

    def get_content(self):
        return self.content

    def populate_content(self) -> None:
        if Utilities.gene_master_data is None:
            Utilities.gene_master_data = load_master_data()

        if self.section_title == "":
            self.section_title = random.choice(
                sorted(Utilities.gene_master_data.keys())
            )

        # content: list of list of three elements [significance: str, include: dict, avoid: list]
