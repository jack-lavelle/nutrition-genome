from scipy import spatial
import gensim.downloader as api
import numpy as np
from Patient import Patient
import string

from Utilities import download_patients, get_gene_info

patients = download_patients()
patient: Patient = patients[0]
patient.objectives = ["Sleep better.", "Lose weight.", "Increase strength."]

# get all gene significances
genes = []
for section in patient.category_genes_dict:
    for gene in patient.category_genes_dict[section]:
        genes.append(gene)

gene_data = {}
for gene in genes:
    gene_data[gene] = get_gene_info(gene)


def preprocess(s):
    # COMT SLOW has significance as a list
    if type(s) == list:
        s = " ".join(s)

    return [
        i.lower()
        for i in s.translate(
            str.maketrans(string.punctuation, "                                ")
        ).split()
    ]


model = api.load("glove-wiki-gigaword-300")


def get_vector(s):
    try:
        return np.sum(np.array([model[i] for i in preprocess(s)]), axis=0)
    except KeyError as e:
        raise KeyError(e)


results = {}


def get_similarity_dict(objective: str):
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
            results.items(), key=lambda v: float(v[1]["Similarity"]), reverse=True
        )
    }

    return important_dict


x = {}
for objective in patient.objectives:
    x[objective] = get_similarity_dict(objective)

print(x)
