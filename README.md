# 🔐 JSON File Encryption & Decryption Tool

This Python project allows you to securely encrypt and decrypt JSON files using password-based encryption with the `cryptography` library. It ensures that sensitive data can be safely stored and shared.

---

## 📁 Features

-   🔑 Password-protected encryption using Fernet (AES)
-   🔐 Encrypt any JSON file into `.enc` format
-   🔓 Decrypt `.enc` files back to readable JSON
-   🧪 Works inside a virtual environment (no global installs)
-   📂 Outputs decrypted data into a new JSON file

---

## 📦 Requirements

-   Python 3.6+
-   `cryptography` package

Install dependencies (after activating virtual environment):

```bash
pip install -r requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone this repository:

```bash
git clone https://github.com/your-username/json-encryption-tool.git
cd json-encryption-tool
```

### 2. Create and activate a virtual environment:

```bash
python -m venv venv
# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 How to Use

### 🔸 Encrypt a JSON File

```python
from encrypt_script import encrypt_json_file

encrypt_json_file("data.json", "your-password", "data.json.enc")
```

### 🔸 Decrypt a JSON File

```python
from decrypt_script import decrypt_json_file

decrypt_json_file("data.json.enc", "your-password", "decrypted_output.json")
```

This will generate a `decrypted_output.json` file with readable content.

---

## 📝 License

MIT License. Use this responsibly.

---

## 🙋‍♂️ Author

Made with ❤️ by [Abhinav Kumar Jha](https://github.com/akj0712)
