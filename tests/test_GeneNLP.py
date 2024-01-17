import sys, os
import pickle

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")
from Patient import Patient

# from ReportGeneSelectionWindow import ReportGeneSelectionWindow
import Utilities
from gene_nlp import GeneNLP
from report_gene_select_window import ReportGeneSelectionWindow


patients = Utilities.download_patients()
patient: Patient = patients[0]
patient.objectives = {
    "Objective 1": "Sleep better.",
    "Objective 2": "Lose weight.",
    "Objective 3": "Increase strength.",
}


def save_dict(d: dict, path: str):
    """Path should not include the file extension since it must be ".pkl".
    Example path: "C://tmp/saved_dict"
    """
    with open(f"{path}.pkl", "wb+") as f:
        pickle.dump(d, f)


def load_dict(path: str) -> dict:
    """Path should not include the file extension since it must be ".pkl".
    Example path: "C://tmp/saved_dict"
    """
    with open(f"{path}.pkl", "rb") as f:
        return pickle.load(f)


# automatic_gene_dict = GeneNLP.get_automatic_genes(patient)
automatic_gene_dict = load_dict("C:\\tmp\\automatic_gene_dict")

# I have saved a res in "C:\\tmp\\objective_genes.pkl" and can use:
# res = load_dict("C:\\tmp\\objective_genes.pkl")
res = {}
for automatic_gene_dict_entry in automatic_gene_dict.items():
    window = ReportGeneSelectionWindow(patient, automatic_gene_dict_entry)
    res[automatic_gene_dict_entry[0]] = window.get_finalized_genes()

print(res)
