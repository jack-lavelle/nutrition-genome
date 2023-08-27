import unittest
import sys
import os


sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")

from Person import Person


class Tests(unittest.TestCase):
    def test_person_initialization(self):
        person = Person("George Washington")

        self.assertIsNotNone(person.genes)

    def test_person_genes(self):
        person = Person("Donald Fagen")
        person.generate_genes()

        self.assertEqual(type(person.genes), dict)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
