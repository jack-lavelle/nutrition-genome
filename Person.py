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


@staticmethod
def convert_json_data_to_patients(json_patient_data: str):
    patients = []
    for name in json_patient_data:
        patient_data = json_patient_data[name]
        genes = patient_data["genes"]
        patients.append(Person(name, genes))

    return patients
