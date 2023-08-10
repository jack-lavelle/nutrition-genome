import random
import json
import requests
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@staticmethod
def retrieve_json_patient_data():
    # TODO: could not connect to the server
    json_key = {"key": "dyqIDK3amOB09U4PSmSDW5FaZiFMNyoCTlmQESTBzh8="}
    response = requests.get(
        "http://127.0.0.1:5000/read", json=json.dumps(json_key), timeout=30
    )
    json_patient_data = json.loads(response.json()["data"])
    json_patient_data.pop("key")

    return json_patient_data


@staticmethod
def load_master_data() -> dict:
    with open("gene_master_data.json", "r") as file:
        Utilities.gene_master_data = json.load(file)

    return Utilities.gene_master_data


class Utilities:
    all_genes = []
    gene_master_data = {}

    @staticmethod
    def generate_genes():
        genes = {}

        for gene_section in load_master_data().keys():
            genes[gene_section] = Utilities.generate_section_genes(gene_section)

        return genes

    @staticmethod
    def generate_section_genes(section_title: str) -> list:
        if not section_title:
            section_title = None

        if not Utilities.gene_master_data:
            load_master_data()

        genes_random_sample = []
        while len(genes_random_sample) == 0:
            genes_random_sample = random.sample(
                sorted(Utilities.gene_master_data[section_title]),
                k=random.randint(0, len(Utilities.gene_master_data[section_title])),
            )
        return genes_random_sample

    @staticmethod
    def get_gene_master_data() -> dict:
        if not Utilities.gene_master_data:
            load_master_data()

        return Utilities.gene_master_data

    @staticmethod
    def gen_section_title() -> str:
        return random.choice(sorted(load_master_data().keys()))

    @staticmethod
    def get_all_genes():
        if not all_genes:
            all_genes = [
                list(
                    Utilities.get_gene_master_data()[
                        list(Utilities.get_gene_master_data().keys())[i]
                    ].keys()
                )
                for i in range(0, len(Utilities.get_gene_master_data().keys()))
            ]

        return all_genes
