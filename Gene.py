class Gene:
    """Class used to represent a single gene taken from `gene_master_data.json`.

    Attributes:
        name (str): Name of gene.
        significance (str): Significance of having the gene in terms of patient health outcomes.
        This is very important for identifying relevant advice for the patient with respect to their
        own personal objectives.
        include (dict[str, list[str]]): This includes relevant advice with sections titled "lifestyle",
        "nutrition", and "supplements".
        avoid (list[str]): This includes what the patient should avoid.
    """

    def __init__(
        self,
        name: str,
        significance: str,
        include: dict[str, list[str]],
        avoid: list[str],
    ) -> None:
        self.name = name
        self.sigificance = significance
        self.include = include
        self.avoid = avoid
