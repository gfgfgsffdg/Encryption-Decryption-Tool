from cryptography.fernet import Fernet
import os
import string
import random
import base64


def generate_key():
    key = Fernet.generate_key()
    with open('encryption.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    with open('encryption.key', 'rb') as key_file:
        return key_file.read()


def get_random_key():
    key_length = 32
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(key_length))


def encrypt_file(file_path, key):
    cipher = Fernet(base64.urlsafe_b64encode(key.encode()))

    with open(file_path, 'rb') as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt_file(file_path, key):
    cipher = Fernet(base64.urlsafe_b64encode(key.encode()))

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)


def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)


def decrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)


def main():
    print('Welcome to the File Encryption/Decryption Tool!')
    print('Please choose an option:')
    print('1. Encrypt file')
    print('2. Decrypt file')
    print('3. Encrypt directory')
    print('4. Decrypt directory')

    choice = input('Enter your choice (1, 2, 3, or 4): ')

    if choice == '1':
        file_path = input('Enter the path to the file you want to encrypt: ')
        key = get_random_key()
        print(f'Generated random key: {key}')
        encrypt_file(file_path, key)
    elif choice == '2':
        file_path = input('Enter the path to the file you want to decrypt: ')
        key = input('Enter the encryption key: ')
        decrypt_file(file_path, key)
    elif choice == '3':
        directory_path = input('Enter the path to the directory you want to encrypt: ')
        key = get_random_key()
        print(f'Generated random key: {key}')
        encrypt_directory(directory_path, key)
    elif choice == '4':
        directory_path = input('Enter the path to the directory you want to decrypt: ')
        key = input('Enter the encryption key: ')
        decrypt_directory(directory_path, key)
    else:
        print('Invalid choice. Please try again.')

    print('Encryption/Decryption completed successfully!')

if __name__ == '__main__':
    main()
