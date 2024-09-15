import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# Encryption
input_text = input("Enter a message to encrypt: ")
result_text = ""

for letter in input_text:
    index = chars.index(letter)
    result_text += key[index]

print(f"Original message: {input_text}")
print(f"Encrypted message: {result_text}")

# Decryption:
encrypted_message = input("Enter a message to decrypt: ")
original_text = ""

for letter in encrypted_message:
    index = key.index(letter)
    original_text += chars[index]

print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {original_text}")
