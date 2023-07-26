import random
import json


class Utilities:
    gene_master_data = {}
    all_genes = []

    @staticmethod
    def generate_genes():
        genes = {}

        for gene_section in Utilities.load_master_data().keys():
            genes[gene_section] = Utilities.generate_section_genes(gene_section)

        return genes

    @staticmethod
    def generate_section_genes(section_title: str) -> list:
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

    @staticmethod
    def get_gene_master_data() -> dict:
        if not Utilities.gene_master_data:
            Utilities.load_master_data()

        return Utilities.gene_master_data

    @staticmethod
    def gen_section_title() -> str:
        return random.choice(sorted(Utilities.load_master_data().keys()))

    @staticmethod
    def get_all_genes():
        if not Utilities.all_genes:
            Utilities.all_genes = [
                list(
                    Utilities.get_gene_master_data()[
                        list(Utilities.get_gene_master_data().keys())[i]
                    ].keys()
                )
                for i in range(0, len(Utilities.get_gene_master_data().keys()))
            ]

        return Utilities.all_genes

    @staticmethod
    def load_patients():
        # TODO
        pass
