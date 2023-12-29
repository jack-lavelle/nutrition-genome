import spacy
from Patient import Patient

from Utilities import download_patients, get_gene_info

# This is currently not being used due to weird situation where all the same genes are almost equally
# relevant to each objective. Example:
# 'Sleep better.':
# {'FUT2': {'Similarity': 0.7191257189400635, 'Significance': 'Lower Gaba productio...lm hormone', 'Category': 'Mood / Memory'}, 'GAD1': {'Similarity': 0.6919629213118819, 'Significance': 'Lower GABA-sleep/calm hormone', 'Category': 'Mood / Memory'}, 'HFE': {'Similarity': 0.6299084748050775, 'Significance': 'Associated with hemo...hromatosis', 'Category': 'General Inflammation'}, 'SHBG rs6258 - Female': {'Similarity': 0.6136377588463395, 'Significance': 'High fructose intake...gen levels', 'Category': 'Hormones'}, 'HLADQ2.5/HLADQ8': {'Similarity': 0.611747402909439, 'Significance': 'Associated with celiac disease', 'Category': 'Gut Health'}, 'SELENBP1': {'Similarity': 0.6084740543003766, 'Significance': 'Associated with low immunity', 'Category': 'Immune System'}, 'VOKRC1*2': {'Similarity': 0.6007015081232634, 'Significance': 'Associated with arte...cification', 'Category': 'Heart Health'}, 'AGTR1 - Male': {'Similarity': 0.585360676683945, 'Significance': 'Higher BP and high fat diet', 'Category': 'Heart Health...
# 'Lose weight.':
# {'FUT2': {'Similarity': 0.7345851482323646, 'Significance': 'Lower Gaba productio...lm hormone', 'Category': 'Mood / Memory'}, 'GAD1': {'Similarity': 0.6839713641382024, 'Significance': 'Lower GABA-sleep/calm hormone', 'Category': 'Mood / Memory'}, 'HFE': {'Similarity': 0.6133692635288356, 'Significance': 'Associated with hemo...hromatosis', 'Category': 'General Inflammation'}, 'HLADQ2.5/HLADQ8': {'Similarity': 0.5981405049157629, 'Significance': 'Associated with celiac disease', 'Category': 'Gut Health'}, 'SELENBP1': {'Similarity': 0.5787205149961179, 'Significance': 'Associated with low immunity', 'Category': 'Immune System'}, 'VOKRC1*2': {'Similarity': 0.5663759446294485, 'Significance': 'Associated with arte...cification', 'Category': 'Heart Health'}, 'NBPF3': {'Similarity': 0.5621710968267564, 'Significance': 'Associated with anxi...n, anxiety', 'Category': 'Brain Health'}, 'PPAR Alpha, homo/heterozygous': {'Similarity': 0.5615495541264457, 'Significance': 'Inability to go into ketosis', 'Category': 'Die...
# 'Increase strength.':
# {'FUT2': {'Similarity': 0.676466661135054, 'Significance': 'Lower Gaba productio...lm hormone', 'Category': 'Mood / Memory'}, 'GAD1': {'Similarity': 0.6755221801033238, 'Significance': 'Lower GABA-sleep/calm hormone', 'Category': 'Mood / Memory'}, 'HFE': {'Similarity': 0.4802144150972043, 'Significance': 'Associated with hemo...hromatosis', 'Category': 'General Inflammation'}, 'HLADQ2.5/HLADQ8': {'Similarity': 0.4782975623263491, 'Significance': 'Associated with celiac disease', 'Category': 'Gut Health'}, 'PPAR Alpha, homo/heterozygous': {'Similarity': 0.46848158248900384, 'Significance': 'Inability to go into ketosis', 'Category': 'Diet'}, 'AGTR1 - Male': {'Similarity': 0.44729848626631363, 'Significance': 'Higher BP and high fat diet', 'Category': 'Heart Health'}, 'AGTR1 - Female': {'Similarity': 0.44729848626631363, 'Significance': 'Higher BP and high fat diet', 'Category': 'Heart Health'}, 'NBPF3': {'Similarity': 0.43691825817580043, 'Significance': 'Associated with anxi...n, anxiety', 'Category': 'Brain ...

patients = download_patients()
patient: Patient = patients[0]
patient.objectives = ["Sleep better.", "Lose weight.", "Increase strength."]

genes = []
for section in patient.category_genes_dict:
    for gene in patient.category_genes_dict[section]:
        genes.append(gene)

gene_data = {}
for gene in genes:
    gene_data[gene] = get_gene_info(gene)

results = {}
nlp = spacy.load("en_core_web_lg")


def get_similarity(objective: str):
    for gene_name, data in gene_data.items():
        significance = data["Significance"]
        if not significance:
            continue

        if isinstance(significance, list):
            significance = " ".join(significance)

        doc = nlp(objective)
        doc2 = nlp(significance)
        results[gene_name] = {
            "Similarity": 1 - doc.similarity(doc2),
            "Significance": significance,
            "Category": data["Category"],
        }

    important_dict = {
        k: v
        for k, v in sorted(
            results.items(), key=lambda v: float(v[1]["Similarity"]), reverse=True
        )
    }
    return important_dict


x = {}
for patient_objective in patient.objectives:
    x[patient_objective] = get_similarity(patient_objective)

print(x)
