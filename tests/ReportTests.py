import unittest
from Gene import Gene
from Patient import Patient


class ReportTests(unittest.TestCase):
    def test_report_generation(self, patient: Patient, selected_genes: list[Gene]):
        report = Report(patient.name, selected_genes)
