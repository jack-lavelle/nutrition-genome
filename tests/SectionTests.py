import unittest
from Section import Section
from Utilities import Utilities


class Tests(unittest.TestCase):
    def test_section_initialization(self):
        section = Section("Heart Health", [])

        self.assertIsNotNone(section.genes)

    def test_gene_generation(self):
        genes = Utilities.generate_genes("Heart Health")

        self.assertIsNotNone(genes)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
