import unittest
from Section import Section


class SectionTests(unittest.TestCase):
    def test_section_initialization(self):
        section = Section("Brain Health")
        section.populate_content()

        self.assertEqual(section.section_title, "Brain Health")


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
