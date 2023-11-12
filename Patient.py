import PatientUtilities


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
    category_genes_dict = {}
    objectives = {}

    def __init__(
        self, name=None, genes=PatientUtilities.generate_genes(), objectives=None
    ) -> None:
        self.name = name
        self.objectives = objectives
        self.category_genes_dict = genes

    def create_report(self):
        # https://github.com/python-openxml/python-docx
        pass
