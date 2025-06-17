from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def decrypt_file(encrypted_file):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_file, "rb") as enc_file:
        encrypted_data = enc_file.read()

    try:
        decrypted = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("Decryption failed:", e)
        return

    # Save output by removing .enc from original name
    if encrypted_file.endswith(".enc"):
        output_file = encrypted_file[:-4]
    else:
        output_file = encrypted_file + "_decrypted"

    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted)

    print(f"Decryption successful! File saved as: {output_file}")

if __name__ == "__main__":
    decrypt_file("mask.txt.docx.enc")

