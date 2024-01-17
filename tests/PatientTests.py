import unittest
import sys
import os


sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")

from Patient import Patient


def is_list_of_strings(lst):
    return all(isinstance(item, str) for item in lst)


class Tests(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.patient = Patient(
            "George Washington",
            None,
            ["Sleep better.", "Lose weight.", "Increase strength."],
        )

    def test_patient_initialization(self):
        self.assertIsNotNone(self.patient.category_genes_dict)

    def test_patient_genes_dict(self):
        self.assertEqual(type(self.patient.category_genes_dict), dict)

    def test_patient_genes_list(self):
        self.assertTrue(is_list_of_strings(self.patient.genes))


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
