import json
from json import JSONEncoder
from cryptography.fernet import Fernet
from Person import Person

secret_key = Fernet.generate_key()


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def encrypt_data(json_data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(json_data)
    return encrypted_data


def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return json.loads(decrypted_data)


def generate_patients():
    patients = {}
    # TODO: store patients by uuid
    # Create random patients

    patients["George Washington"] = Person("George Washington")
    patients["Abraham Lincoln"] = Person("Abraham Lincoln")

    json_patients = json.dumps(patients, cls=MyEncoder).encode("utf-8")
    # loaded_patients = json.loads(saved_patients)

    return json_patients


key = b"dyqIDK3amOB09U4PSmSDW5FaZiFMNyoCTlmQESTBzh8="
encrypted = encrypt_data(generate_patients(), key)

print(decrypt_data(encrypted, key))
