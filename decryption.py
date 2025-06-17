from cryptography.fernet import Fernet
import json
import base64
import hashlib

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def decrypt_json_file(enc_file_path, password, output_path="decrypted_data.json"):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(enc_file_path, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data).decode()
    
    json_data = json.loads(decrypted_data)

    with open(output_path, 'w') as out_file:
        json.dump(json_data, out_file, indent=4)

    print(f"Decrypted data saved to: {output_path}")

# Example usage
json_data = decrypt_json_file("sample.json.enc", "your-password")
