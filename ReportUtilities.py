from scipy import spatial
import gensim.downloader as api
import numpy as np

from Patient import Patient


def example():
    """This was taken from: https://stackoverflow.com/questions/65852710/text-similarity-using-word2vec"""
    model = api.load(
        "glove-wiki-gigaword-50"
    )  # choose from multiple models https://github.com/RaRe-Technologies/gensim-data

    s0 = "Mark zuckerberg owns the facebook company"
    s1 = "Facebook company ceo is mark zuckerberg"
    s2 = "Microsoft is owned by Bill gates"
    s3 = "How to learn japanese"

    def get_vector(s):
        def preprocess(s):
            return [i.lower() for i in s.split()]

        return np.sum(np.array([model[i] for i in preprocess(s)]), axis=0)

    print("s0 vs s1 ->", 1 - spatial.distance.cosine(get_vector(s0), get_vector(s1)))
    print("s0 vs s2 ->", 1 - spatial.distance.cosine(get_vector(s0), get_vector(s2)))
    print("s0 vs s3 ->", 1 - spatial.distance.cosine(get_vector(s0), get_vector(s3)))


def get_relevant_genes(patient: Patient) -> list:
    """This will return relevant genes"""
