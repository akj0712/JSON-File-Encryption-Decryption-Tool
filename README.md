# JSON File Encryption & Decryption Tool 🛡️

A Python-based tool to **securely encrypt and decrypt JSON files** using AES (Fernet) encryption, with a **GUI interface for file selection**. Ensures that encrypted files are **tamper-proof** and **read-only**, providing strong cryptographic guarantees.

---

## 🔐 Features

-   🔒 AES encryption with Fernet (symmetric key)
-   🔑 Password-based key derivation (SHA-256)
-   📁 File Explorer GUI for selecting input and output files
-   🧪 Built-in cryptographic tamper detection (via HMAC)
-   🧱 Automatically sets `.enc` file to read-only after encryption
-   ❌ Decryption fails on any tampering or wrong password
-   🔁 Password prompt with up to 3 retry attempts (for decryption)

---

## 🛠 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/JSON-File-Encryption-Decryption-Tool.git
cd JSON-File-Encryption-Decryption-Tool
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Mac: source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔐 Encrypt a JSON File

```bash
python encryption.py
```

-   Choose a `.json` file using the file explorer.
-   Enter a password.
-   Choose where to save the encrypted file (`.enc`).
-   The file will be encrypted and made **read-only** automatically.

### 🔓 Decrypt an `.enc` File

```bash
python decryption.py
```

-   Choose an encrypted `.enc` file.
-   Enter the correct password (3 attempts allowed).
-   Choose where to save the decrypted `.json` file.

---

## 📂 File Structure

```
JSON-File-Encryption-Decryption-Tool/
├── encryption.py           # Encrypts a selected JSON file
├── decryption.py           # Decrypts an encrypted .enc file
├── requirements.txt        # Project dependencies
└── README.md               # You’re reading it
```

---

## 📦 Dependencies

-   `cryptography`
-   `tkinter` (standard with Python)
-   `hashlib`, `base64`, `os`, `json` (standard libs)

Install all via:

```bash
pip install -r requirements.txt
```

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## 📢 Notes

-   This tool **does not store your password**. If you forget it, the file **cannot** be decrypted.
-   Encryption is **cryptographically secure and tamper-evident** using Fernet (AES + HMAC).

---

> Built with ❤️ using Python by [Abhinav Kumar Jha](https://github.com/akj0712)

```
Happy encrypting! 🔐
```
