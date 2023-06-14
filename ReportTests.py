import unittest
from Section import Section
from Report import Report
from Person import Person
from Utilities import Utilities


class ReportTests(unittest.TestCase):
    def report_section_initialization(self, section):
        section = Section("Brain Health", None)
        section.populate_content()

        batman = Person("Batman")
        batman.set_genes(
            Utilities.generate_genes(
                self,
                gene_master_data=Utilities.load_master_data(self),
                section_title=Utilities.gen_section_title(section),
            )
        )
        report = Report("Batman")
        
    def generate_report_pdf(self):
        
        
