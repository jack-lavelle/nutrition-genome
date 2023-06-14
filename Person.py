class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.gene_dict = {}
        self.reportsDict = {}

    def add_gene(self, gene, phenotype):
        self.gene_dict[gene] = phenotype

    def set_genes(self, genes):
        self.gene_dict = genes

    def add_report(self, date):
        pass
