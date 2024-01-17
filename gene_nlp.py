# These are needed to prevent circular imports when using type checking.
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Patient import Patient

from scipy import spatial
import gensim.downloader as api
import numpy as np
import string

from Utilities import get_gene_info


class GeneNLP:
    @staticmethod
    def get_automatic_genes(patient: Patient) -> dict[str, dict]:
        # TODO: refactor
        """This is responsible for calling the NLP model and returning a dict consisting of the
        objectives of a patient with the genes selected using the NLP model.

        Example output:
        {
            "Objective 1: Sleep better.": {
                "MTHFR 1298": {
                    "Similarity": 0.6009981632232666,
                    "Significance": "Higher need for fola...rotection)",
                    "Category": "General Inflammation"
                },
                "GAD1": {
                    "Similarity": 0.5977962017059326,
                    "Significance": "Lower GABA-sleep/calm hormone",
                    "Category": "Mood / Memory"
                },
                "FUT2": {
                    "Similarity": 0.5956557393074036,
                    "Significance": "Lower Gaba productio...lm hormone",
                    "Category": "Mood / Memory"
                }
            },
            "Objective 2: Lose weight.": {
                ...
            }
        }
        """
        model = api.load("glove-wiki-gigaword-300")

        def preprocess(s):
            # COMT SLOW has significance as a list
            if type(s) == list:
                s = " ".join(s)

            return [
                i.lower()
                for i in s.translate(
                    str.maketrans(
                        string.punctuation, "                                "
                    )
                ).split()
            ]

        def get_vector(s):
            try:
                return np.sum(np.array([model[i] for i in preprocess(s)]), axis=0)
            except KeyError as e:
                raise KeyError(e)

        objective_important_dict = {}
        gene_data = {}
        for gene in patient.genes:
            gene_data[gene] = get_gene_info(gene)

        for objective_number, objective in patient.objectives.items():
            results = {}
            for gene, data in gene_data.items():
                significance = data["Significance"]
                if not significance:
                    continue
                try:
                    results[gene] = {
                        "Similarity": 1
                        - spatial.distance.cosine(
                            get_vector(objective), get_vector(significance)
                        ),
                        "Significance": significance,
                        "Category": data["Category"],
                    }
                except KeyError as e:
                    print(e)

            important_dict = {
                k: v
                for k, v in sorted(
                    results.items(),
                    key=lambda v: float(v[1]["Similarity"]),
                    reverse=True,
                )
            }
            d = {}
            for i, entry in enumerate(important_dict.items()):
                if i == 3:
                    break
                d[entry[0]] = entry[1]

            objective_important_dict[f"{objective_number}: {objective}"] = d
        return objective_important_dict
