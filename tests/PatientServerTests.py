import sys
import os

# TODO: rework all paths to be operating system agnostic
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")
import unittest

unittest.TestLoader.sortTestMethodsUsing = None

from Patient import Patient
import Utilities

# TODO: add delete patient data button
# TODO: handle empty data


class Tests(unittest.TestCase):
    def test_a_upload_patients(self):
        patients = []

        # TODO: store patients by uuid
        names = ["George Washington", "Abraham Lincoln", "Gandalf"]
        for name in names:
            patient = Patient(name)
            patient.objectives = {
                "objective 1": "Destroy the jedi.",
                "objective 2": "Crush the rebellion.",
                "objective 3": "Make Luke my apprentice.",
            }
            patients.append(patient)

        response = Utilities.upload_patients(patients)
        self.assertEqual(response.status_code, 200)

    def test_b_download_patients(self):
        patients = Utilities.download_patients()

        self.assertEqual(type(patients[0]), Patient)

    def test_c_delete_patient(self):
        Utilities.delete_patient("George Washington")
        patients = Utilities.download_patients()
        self.assertNotIn("George Washington", patients)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
