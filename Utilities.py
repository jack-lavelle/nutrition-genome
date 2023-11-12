import random
import json
import requests
from requests import Response
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@staticmethod
# TODO: refactor this ... rename to `download_patients`, set typing more accurately, etc
def download_patients() -> list:
    from Patient import Patient

    # TODO: could not connect to the server
    json_key = {"key": "dyqIDK3amOB09U4PSmSDW5FaZiFMNyoCTlmQESTBzh8="}
    response = requests.get(
        "https://genomenutrition.pythonanywhere.com/read",
        json=json.dumps(json_key),
        timeout=30,
    )
    json_patient_data = json.loads(response.json()["data"])
    json_patient_data.pop("key")

    patients = []
    for name in json_patient_data:
        patient_data = json_patient_data[name]
        genes = patient_data["genes"]
        objectives = patient_data["objectives"]
        patients.append(Patient(name, genes, objectives))

    return patients


@staticmethod
# TODO patients should be `dict[str, Patient]` not a list
def upload_patients(patients: list) -> Response:
    data = {}
    for patient in patients:
        data[patient.name] = patient

    data["key"] = "dyqIDK3amOB09U4PSmSDW5FaZiFMNyoCTlmQESTBzh8="

    # TODO: handle this failing
    return requests.post(
        "https://genomenutrition.pythonanywhere.com/save",
        json=json.dumps(data, cls=MyEncoder),
        timeout=30,
    )


@staticmethod
def delete_patient(name: str) -> bool:
    patients = download_patients()
    patients_dict = {}
    for patient in patients:
        patients_dict[patient.name] = patient

    patients_dict.pop(name)
    updated_patients = []
    for patient in patients_dict.items():
        updated_patients.append(patient[1])
    upload_patients(updated_patients)
    return True


@staticmethod
def load_master_data() -> dict:
    with open("gene_master_data.json", "r", encoding="utf-8") as file:
        Utilities.gene_master_data = json.load(file)

    return Utilities.gene_master_data


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
def get_gene_info(gene: str) -> dict:
    gene_info = {}
    gene_master_data = get_gene_master_data()

    # Find gene category.
    for section in gene_master_data:
        if gene in gene_master_data[section]:
            gene_info["Category"] = section
            return gene_info | gene_master_data[section][gene]


class Utilities:
    # Almost certain this class should be removed at some point.
    all_genes = []
    gene_master_data = {}

    @staticmethod
    def gen_section_title() -> str:
        return random.choice(sorted(load_master_data().keys()))

    @staticmethod
    def get_all_genes():
        if not all_genes:
            all_genes = [
                list(
                    get_gene_master_data()[
                        list(get_gene_master_data().keys())[i]
                    ].keys()
                )
                for i in range(0, len(get_gene_master_data().keys()))
            ]

        return all_genes

    @staticmethod
    def categorize_genes() -> list[list]:
        gene_master_data = load_master_data()
        gene_sections = list(gene_master_data.keys())
        gene_groups = []
        gene_group = []
        gene_count = 0

        for gene_section in gene_sections:
            number_of_genes_in_section = len(
                list(gene_master_data[gene_section].keys())
            )

            if gene_count + number_of_genes_in_section <= 20:
                gene_group.append(gene_section)
                gene_count += number_of_genes_in_section
            else:
                gene_groups.append(gene_group)
                gene_group = [gene_section]
                gene_count = number_of_genes_in_section

        gene_groups.append(gene_group)
        return gene_groups
