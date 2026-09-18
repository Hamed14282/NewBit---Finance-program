import os

from cryptography.fernet import Fernet

def check_key():
    global key

    if not os.path.exists("data/users.key"):
        with open("data/users.key", "wb") as key_file:
            key_file.write(Fernet.generate_key())
    with open("data/users.key", "rb") as key_file:
        key = key_file.read()
        
def decrypt_file(path):
    global key, decrypted
    
    cypher = Fernet(key)

    with open(path, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    if not encrypted == b"":
        decrypted = cypher.decrypt(encrypted)

        with open(path, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
    else:
        decrypted = b""

    return decrypted

def encrypt_file(path):
    global key
    cypher = Fernet(key)

    with open("data/users.csv", "rb") as decrypted_file:
        decrypted = decrypted_file.read()

    encrypted = cypher.encrypt(decrypted)

    with open("data/users.csv", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

check_key()
encrypt_file("data/users.csv")