import Patient
from Section import Section


class Report:
    def __init__(self, patient: Patient):
        self.patient = patient
        self.sections_dict = {}

    def setSectionsDict(self, sections_dict: dict):
        self.sections_dict = sections_dict

    def addSection(self, section_title: str, genes: list) -> Section:
        self.sections_dict[section_title] = Section(section_title, genes)
