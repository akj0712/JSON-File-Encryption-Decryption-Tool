from cryptography.fernet import Fernet
import json
import base64
import hashlib
from tkinter import Tk, filedialog
import os

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def decrypt_json_file(password, output_path="decrypted_data.json"):
    # Hide the root window
    root = Tk()
    root.withdraw()

    # Open file dialog to select encrypted .enc file
    enc_file_path = filedialog.askopenfilename(
        title="Select Encrypted File to Decrypt",
        filetypes=[("Encrypted Files", "*.enc")],
    )

    if not enc_file_path:
        print("No file selected.")
        return

    key = generate_key(password)
    fernet = Fernet(key)

    try:
        with open(enc_file_path, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data).decode()
        json_data = json.loads(decrypted_data)

        with open(output_path, 'w') as out_file:
            json.dump(json_data, out_file, indent=4)

        print(f"Decrypted data saved to: {output_path}")
    except Exception as e:
        print("Decryption failed:", str(e))

# Example usage
decrypt_json_file("your-password")
