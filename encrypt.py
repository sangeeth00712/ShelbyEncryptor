from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as key.key")

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)
    encrypted_filename = filename + ".enc"

    with open(encrypted_filename, "wb") as enc_file:
        enc_file.write(encrypted)

    print(f"Encrypted file saved as: {encrypted_filename}")

if __name__ == "__main__":
    # Run this once to generate the key
    generate_key()

    # Replace this with your real file name
    encrypt_file("mask.txt.docx")

