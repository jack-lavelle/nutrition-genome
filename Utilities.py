import random
import json


class Utilities:
    gene_master_data = {}

    @staticmethod
    def generate_genes(section_title: str) -> list:
        if not section_title:
            section_title = None

        if not Utilities.gene_master_data:
            Utilities.load_master_data()

        genes_random_sample = []
        while len(genes_random_sample) == 0:
            genes_random_sample = random.sample(
                sorted(Utilities.gene_master_data[section_title]),
                k=random.randint(0, len(Utilities.gene_master_data[section_title])),
            )
        return genes_random_sample

    @staticmethod
    def load_master_data() -> dict:
        with open("gene_master_data.json", "r") as file:
            Utilities.gene_master_data = json.load(file)

        return Utilities.gene_master_data

    def gen_section_title(self) -> str:
        return random.choice(sorted(self.load_master_data().keys()))
