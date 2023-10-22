import Utilities


@staticmethod
def generate_genes():
    genes = {}

    for gene_section in Utilities.load_master_data().keys():
        genes[gene_section] = Utilities.generate_section_genes(gene_section)

    return genes
