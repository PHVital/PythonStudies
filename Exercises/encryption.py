import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plainText = input("Enter a message to encrypt: ")
cipherText = ""

for letter in plainText:
    index = chars.index(letter)
    cipherText += key[index]

print(f"Original message: {plainText}")
print(f"Encrypted message: {cipherText}")

cipherText = input("Enter a message to encrypt: ")
plainText = ""

for letter in cipherText:
    index = key.index(letter)
    plainText += chars[index]

print(f"Encrypted message: {cipherText}")
print(f"Original message: {plainText}")