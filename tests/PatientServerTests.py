import sys
import os

# TODO: rework all paths to be operating system agnostic
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")
import unittest

from Patient import Patient, convert_json_data_to_patients
import Utilities

# TODO: add delete patient data button
# TODO: handle empty data


class Tests(unittest.TestCase):
    def test_upload_patients(self):
        patients = []

        # TODO: store patients by uuid
        names = ["George Washington", "Abraham Lincoln", "Gandalf"]
        for name in names:
            patients.append(Patient(name))

        response = Utilities.upload_patients(patients)
        self.assertEqual(response.status_code, 200)

    def test_download_patients(self):
        json_patient_data = Utilities.retrieve_json_patient_data()
        patients = convert_json_data_to_patients(json_patient_data)

        self.assertEqual(type(patients[0]), Patient)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
