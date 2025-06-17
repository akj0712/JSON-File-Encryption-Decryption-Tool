from cryptography.fernet import Fernet
import json
import base64
import hashlib
from tkinter import Tk, filedialog
import os

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_json_file(password):
    # Hide the root window
    root = Tk()
    root.withdraw()

    # Open file explorer dialog
    file_path = filedialog.askopenfilename(
        title="Select JSON File to Encrypt",
        filetypes=[("JSON Files", "*.json")],
    )

    if not file_path:
        print("No file selected.")
        return

    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, 'r') as file:
        data = file.read()

    encrypted = fernet.encrypt(data.encode())

    enc_file_path = file_path + ".enc"
    with open(enc_file_path, 'wb') as file:
        file.write(encrypted)

    print("Encrypted and saved as", enc_file_path)

# Example usage
encrypt_json_file("your-password")
