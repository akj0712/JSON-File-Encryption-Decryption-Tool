from cryptography.fernet import Fernet
import json
import base64
import hashlib

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_json_file(file_path, password):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, 'r') as file:
        data = file.read()

    encrypted = fernet.encrypt(data.encode())
    
    with open(file_path + ".enc", 'wb') as file:
        file.write(encrypted)

    print("Encrypted and saved as", file_path + ".enc")

# Example usage
encrypt_json_file("sample.json", "your-password")
