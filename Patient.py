from Utilities import Utilities


class Patient:
    # TODO: finish this docstring
    """Contains information for a patient.

    Attributes:
        name (`str`): Name of the patient.
        reportsDict (`dict`): Meant to serve as a way to retrieve previous reports, where keys are
            the date of creation and values are the path to the report.
        genes (`dict`):
    """

    name = None
    reportsDict = {}
    genes = {}
    objectives = {}

    def __init__(
        self, name=None, genes=Utilities.generate_genes(), objectives=None
    ) -> None:
        self.name = name
        if not objectives:
            self.objectives = {
                "objective 1": "Destroy the jedi.",
                "objective 2": "Crush the rebellion.",
                "objective 3": "Make Luke my apprentice.",
            }
        self.genes = genes

    def add_report(self, date):
        pass


@staticmethod
def convert_json_data_to_patients(json_patient_data: dict):
    patients = []
    for name in json_patient_data:
        patient_data = json_patient_data[name]
        genes = patient_data["genes"]
        patients.append(Patient(name, genes))

    return patients
