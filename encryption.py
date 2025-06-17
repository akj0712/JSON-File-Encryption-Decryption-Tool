from cryptography.fernet import Fernet
import json
import base64
import hashlib
from tkinter import Tk, filedialog, simpledialog
import os
import stat

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_json_file():
    # Initialize hidden Tkinter root
    root = Tk()
    root.withdraw()

    # File selection
    file_path = filedialog.askopenfilename(
        title="Select JSON File to Encrypt",
        filetypes=[("JSON Files", "*.json")],
    )
    if not file_path:
        print("No file selected.")
        return

    # Prompt for password
    password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
    if not password:
        print("Encryption cancelled: No password entered.")
        return

    # Choose where to save the encrypted file
    output_path = filedialog.asksaveasfilename(
        title="Save Encrypted File As",
        defaultextension=".enc",
        filetypes=[("Encrypted Files", "*.enc")],
        initialfile=os.path.basename(file_path) + ".enc"
    )
    if not output_path:
        print("No output file selected.")
        return

    try:
        # Encrypt the file
        with open(file_path, 'r') as file:
            data = file.read()

        key = generate_key(password)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data.encode())

        with open(output_path, 'wb') as file:
            file.write(encrypted)

        # Make file read-only
        os.chmod(output_path, stat.S_IREAD)  # On Unix-like systems
        # On Windows, to ensure it's also read-only at OS level:
        if os.name == 'nt':
            os.system(f'attrib +R "{output_path}"')

        print("Encrypted and saved to:", output_path)
        print("File is now read-only.")
    except Exception as e:
        print("Encryption failed:", str(e))

# Run the function
encrypt_json_file()
