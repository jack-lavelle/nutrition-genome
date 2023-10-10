from Utilities import Utilities


class Person:
    name = None
    reportsDict = {}
    genes = {}

    def __init__(self, name=None, genes=None) -> None:
        self.name = name
        if not genes:
            patient_genes = {}
            for gene_section in list(Utilities.gene_master_data.keys()):
                patient_genes[gene_section] = {}
            self.genes = patient_genes
        else:
            self.genes = genes

    def generate_genes(self):
        self.genes = Utilities.generate_genes()

    def add_report(self, date):
        pass


@staticmethod
def convert_json_data_to_patients(json_patient_data: dict):
    patients = []
    for name in json_patient_data:
        patient_data = json_patient_data[name]
        genes = patient_data["genes"]
        patients.append(Person(name, genes))

    return patients
