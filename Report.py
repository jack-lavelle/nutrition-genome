from Patient import Patient
from Gene import Gene
from docx import Document


class Report:
    """A Report is characterized by the patient, their objectives (at that time), and specific 
    selection of genes chosen for the report. 
    
    Attributes:
        patient (`Patient`): the patient who the report is created for.
        
        objective_genes_map (`dict[str, dict[str, list[Gene]]]`): this is best explained by example,
        but a brief description is that this is what links a patient's objectives to the advice
        selected by the genes whose significance relates to a particular objective at hand. Example:
        
        {
            "Objective 1" : {
                "Category 1" : [
                    "Gene 1", <-- call get_gene_info(...) here
                    "Gene 2"
                ],
                "Category 2" : [
                    "Gene 1",
                    "Gene 2"
                ]
            },
            "Objective 2" : {
                "Category 1" : [
                    "Gene 1", 
                    "Gene 2",
                    "Gene 3"
                ]
            }
        }
        
        
    """
    def __init__(self, patient: Patient, objective_genes_map: dict[str, dict[str, list[Gene]]]):
        self.patient = patient
        self.objective_genes_map = objective_genes_map
        
    def generate(self):
        # TODO need a selection of genes that is derived from BOTH 1) manual, and 2) automatic gene
        # selection.
