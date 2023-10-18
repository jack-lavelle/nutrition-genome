import unittest
import sys
import os


sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")

from Patient import Patient


class Tests(unittest.TestCase):
    def test_patient_initialization(self):
        patient = Patient("George Washington")

        self.assertIsNotNone(patient.genes)

    def test_patient_genes(self):
        patient = Patient("Donald Fagen")
        patient.generate_genes()

        self.assertEqual(type(patient.genes), dict)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
