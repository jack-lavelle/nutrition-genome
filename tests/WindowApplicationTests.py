import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")

from Utilities import Utilities


class Tests(unittest.TestCase):
    def test_categorize_genes(self):
        self.assertTrue(all_elements_len_less_than_n(Utilities.categorize_genes(), 20))


def all_elements_len_less_than_n(test_list: list, n: int) -> bool:
    for sublist in test_list:
        if len(sublist) > n:
            return False

    return True


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
