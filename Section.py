import json
import random
from Utilities import Utilities


class Section:
    gene_master_data = None
    section_title = None
    gene_master_data = None

    # a Section corresponds to the data from a number of genes from a single category
    def __init__(self, section_title, genes):
        # TODO: optional section_title
        self.section_title = section_title
        self.gene_master_data = None
        self.content = {}
        self.genes = genes

        if self.genes is not None:
            self.set_content(self.genes)
        else:
            self.content = Utilities.load_master_data(self)

    def set_content(self, genes: list):
        self.handle_genes(genes)

    def get_content(self):
        return self.content

    def populate_content(self) -> list:
        if self.gene_master_data is None:
            self.gene_master_data = Utilities.load_master_data(self)

        if self.section_title == "":
            self.section_title = random.choice(sorted(self.gene_master_data.keys()))

        # content: list of list of three elements [significance: str, include: dict, avoid: list]

        self.handle_genes(
            Utilities.generate_genes(self, self.gene_master_data, self.section_title)
        )

    def handle_genes(self, genes: list):
        for gene in genes:
            specific_gene_data = self.gene_master_data[self.section_title][gene]
            self.content[gene] = {
                "Significance": specific_gene_data["Significance"],
                "Include": specific_gene_data["Include"],
                "Avoid": specific_gene_data["Avoid"],
            }
