from cryptography.fernet import Fernet
import json
import base64
import hashlib
from tkinter import Tk, filedialog, simpledialog, messagebox
import os

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def decrypt_json_file():
    # Initialize hidden Tkinter root
    root = Tk()
    root.withdraw()

    # Select encrypted file
    enc_file_path = filedialog.askopenfilename(
        title="Select Encrypted File to Decrypt",
        filetypes=[("Encrypted Files", "*.enc")],
    )
    if not enc_file_path:
        print("No file selected.")
        return

    # Try password up to 3 times
    decrypted_data = None
    for attempt in range(3):
        password = simpledialog.askstring("Password", f"Enter decryption password (Attempt {attempt+1}/3):", show='*')
        if not password:
            print("Decryption cancelled.")
            return

        key = generate_key(password)
        fernet = Fernet(key)

        try:
            with open(enc_file_path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data).decode()
            break  # successful decryption
        except Exception:
            messagebox.showerror("Error", "Incorrect password. Please try again.")

    if decrypted_data is None:
        print("Decryption failed: Maximum attempts reached.")
        return

    # Choose output save location
    original_name = os.path.basename(enc_file_path)
    name_without_ext = original_name.replace(".json.enc", "").replace(".enc", "")
    initial_file_name = f"decrypted_{name_without_ext}.json"

    output_path = filedialog.asksaveasfilename(
        title="Save Decrypted JSON As",
        defaultextension=".json",
        filetypes=[("JSON Files", "*.json")],
        initialfile=initial_file_name
    )
    if not output_path:
        print("No output file selected.")
        return

    # Save decrypted JSON
    try:
        json_data = json.loads(decrypted_data)
        with open(output_path, 'w') as out_file:
            json.dump(json_data, out_file, indent=4)
        print("Decrypted data saved to:", output_path)
    except Exception as e:
        messagebox.showerror("Error", "Failed to save decrypted data.")
        print("Error saving file:", str(e))

# Run
decrypt_json_file()
