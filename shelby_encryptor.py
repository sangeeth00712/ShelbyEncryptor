import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

backend = default_backend()
salt = b'shelby_salt_'  # You can store/load this from a file for custom handling

def derive_key(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        key = derive_key(password)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open(file_path + ".enc", 'wb') as f:
            f.write(encrypted)
        messagebox.showinfo("Success", f"File encrypted:\n{file_path}.enc")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        key = derive_key(password)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_data)
        original_path = file_path.replace(".enc", "")
        with open(original_path, 'wb') as f:
            f.write(decrypted)
        messagebox.showinfo("Success", f"File decrypted:\n{original_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file_encrypt():
    path = filedialog.askopenfilename()
    if path:
        pwd = password_entry.get()
        if not pwd:
            messagebox.showwarning("Input Needed", "Please enter a password.")
        else:
            encrypt_file(path, pwd)

def browse_file_decrypt():
    path = filedialog.askopenfilename()
    if path:
        pwd = password_entry.get()
        if not pwd:
            messagebox.showwarning("Input Needed", "Please enter a password.")
        else:
            decrypt_file(path, pwd)

# GUI
root = tk.Tk()
root.title("ShelbyEncryptor")
root.geometry("400x200")

tk.Label(root, text="Enter Password:", font=("Helvetica", 12)).pack(pady=10)
password_entry = tk.Entry(root, show='*', width=30, font=("Helvetica", 12))
password_entry.pack(pady=5)

tk.Button(root, text="Encrypt File", command=browse_file_encrypt, width=20, bg="#90ee90").pack(pady=10)
tk.Button(root, text="Decrypt File", command=browse_file_decrypt, width=20, bg="#f08080").pack(pady=5)

root.mainloop()

