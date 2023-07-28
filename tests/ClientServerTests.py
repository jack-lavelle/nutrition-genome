import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")

import json
import requests
import unittest

from Person import Person
from Utilities import MyEncoder


class Tests(unittest.TestCase):
    def test_upload_patients(self):
        patients = {}
        # TODO: store patients by uuid
        names = ["George Washington", "Abraham Lincoln", "Gandalf"]
        for name in names:
            patients[name] = Person(name)

        response = requests.post(
            "http://127.0.0.1:5000/save",
            json=json.dumps(patients, cls=MyEncoder),
            timeout=30,
        )

        self.assertEqual(response.status_code, 200)

    def test_download_patients(self):
        response = requests.get("http://127.0.0.1:5000/read")
        patients = json.loads(response.json()["data"])

        self.assertEqual(type(patients), dict)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
