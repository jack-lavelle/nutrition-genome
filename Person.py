from Utilities import Utilities


class Person:
    name = None
    reportsDict = {}
    genes = {}

    def __init__(self, name, genes=None) -> None:
        self.name = name
        if genes:
            self.genes = genes
        else:
            self.genes = Utilities.generate_genes()

    def add_report(self, date):
        pass
