# File Encryption/Decryption Tool

This Python script provides a simple command-line interface for encrypting and decrypting files or directories using the Fernet symmetric key encryption algorithm from the `cryptography` library.

## Prerequisites
- Python 3
- `cryptography` library (install using `pip install cryptography`)

## Usage

### 1. Encrypting a File
To encrypt a single file, choose option 1, and provide the path to the file you want to encrypt. A random key will be generated, and the file will be encrypted using this key.

### 2. Decrypting a File
To decrypt a single file, choose option 2, and provide the path to the file you want to decrypt. You will be prompted to enter the encryption key used for encryption.

### 3. Encrypting a Directory
To encrypt all files in a directory, choose option 3, and provide the path to the directory. A random key will be generated, and each file in the directory will be encrypted using this key.

### 4. Decrypting a Directory
To decrypt all files in a directory, choose option 4, and provide the path to the directory. You will be prompted to enter the encryption key used for encryption.

## Important Notes
- Keep the encryption key (`encryption.key`) secure. Losing the key will result in irreversible data loss.
- Ensure that you have a backup of the original files before performing decryption.

## Running the Script
```bash
python script_name.py
```

## Disclaimer
This tool is provided as-is, without any warranty. Use it responsibly and at your own risk.

## Contributions
Contributions and improvements are welcome. Feel free to submit issues or pull requests.

## License
This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
