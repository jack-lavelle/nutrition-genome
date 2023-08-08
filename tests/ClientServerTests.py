import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")

import json
import requests
import unittest

from Person import Person
from Utilities import MyEncoder


class Tests(unittest.TestCase):
    def test_upload_data(self):
        data = {}
        # TODO: store patients by uuid
        names = ["George Washington", "Abraham Lincoln", "Gandalf"]
        for name in names:
            data[name] = Person(name)

        data["key"] = "dyqIDK3amOB09U4PSmSDW5FaZiFMNyoCTlmQESTBzh8="
        response = requests.post(
            "http://127.0.0.1:5000/save",
            json=json.dumps(data, cls=MyEncoder),
            timeout=30,
        )

        self.assertEqual(response.status_code, 200)

    def test_download_data(self):
        data = {"key": "dyqIDK3amOB09U4PSmSDW5FaZiFMNyoCTlmQESTBzh8="}
        response = requests.get(
            "http://127.0.0.1:5000/read", json=json.dumps(data), timeout=30
        )
        data = json.loads(response.json()["data"])

        self.assertEqual(type(data), dict)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
