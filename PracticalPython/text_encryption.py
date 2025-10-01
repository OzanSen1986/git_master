import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

#ENCRYPTION TEXT MESSAGES

plain_text = input("Enter a message to be encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original text message  : {plain_text}")
print(f"Encrypted message : {cipher_text}")

#DECRYPTION TEXT MESSAGES

cipher_text = input("Enter a message to be decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Decrypted message : {cipher_text}")
print(f"Original text message  : {plain_text}")

