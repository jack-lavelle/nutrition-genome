import random
import json


class Utilities:
    def generate_genes(self, gene_master_data, section_title):
        if not section_title:
            section_title = None

        if not gene_master_data:
            self.load_master_data()

        genes_random_sample = []
        while len(genes_random_sample) == 0:
            genes_random_sample = random.sample(
                sorted(gene_master_data[section_title]),
                k=random.randint(0, len(gene_master_data[section_title])),
            )
        return genes_random_sample

    def load_master_data(self):
        gene_master_data = {}
        with open("gene_master_data.json", "r") as file:
            gene_master_data = json.load(file)

        return gene_master_data

    def gen_section_title(self):
        return random.choice(sorted(self.load_master_data().keys()))
