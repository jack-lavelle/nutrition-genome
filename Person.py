from Utilities import Utilities


class Person:
    name = None
    reportsDict = {}

    def __init__(self, name, gene_section_title=None) -> None:
        self.genes = {}
        self.name = name
        if not gene_section_title:
            gene_section_title = "Heart Health"

        self.genes[gene_section_title] = Utilities.generate_genes(gene_section_title)

    def set_genes(self, genes):
        self.genes = genes

    def add_report(self, date):
        pass

    def add_dict_genes(self, section_title):
        genes = Utilities.generate_genes(section_title)
        return genes
