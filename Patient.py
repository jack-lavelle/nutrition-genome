import PatientUtilities


class Patient:
    """Contains information for a patient.

    Attributes:
        name (`str`): Name of the patient.

        objectives (`list`): List of the three goals the patient currently has.

        category_genes_dict (`dict`): Contains all the genes a patient has and groups them by
            their category.
    """

    def __init__(self, name, category_genes_dict, objectives) -> None:
        self.name = name
        self.objectives = objectives

        if not category_genes_dict:
            # TODO: Log this rather than print.
            print("No genes given.")
            category_genes_dict = PatientUtilities.generate_genes()

        self.category_genes_dict = category_genes_dict
