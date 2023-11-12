import unittest
import sys
import os


sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")

from Patient import Patient


class Tests(unittest.TestCase):
    def test_patient_initialization(self):
        patient = Patient("George Washington")

        self.assertIsNotNone(patient.category_genes_dict)

    def test_patient_genes(self):
        patient = Patient("Donald Fagen")

        self.assertEqual(type(patient.category_genes_dict), dict)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
