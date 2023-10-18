import sys
import os

# TODO: rework all paths to be operating system agnostic
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")

import json
import requests
import unittest

import Patient
import Utilities


class Tests(unittest.TestCase):
    def test_upload_data(self):
        data = {}
        # TODO: store patients by uuid
        names = ["George Washington", "Abraham Lincoln", "Gandalf"]
        for name in names:
            data[name] = Patient.Patient(name)

        data["key"] = "dyqIDK3amOB09U4PSmSDW5FaZiFMNyoCTlmQESTBzh8="
        response = requests.post(
            "http://127.0.0.1:5000/save",
            json=json.dumps(data, cls=Utilities.MyEncoder),
            timeout=30,
        )

        self.assertEqual(response.status_code, 200)

    def test_download_patients(self):
        json_patient_data = Utilities.retrieve_json_patient_data()
        patients = Patient.convert_json_data_to_patients(json_patient_data)

        self.assertEqual(type(patients[0]), Patient.Patient)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
