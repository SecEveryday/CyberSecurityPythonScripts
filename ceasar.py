ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

def ceasar_encrypt(plain_text):
    cipher_text = ''
    plain_text = plain_text.upper()
    for c in plain_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_text += ALPHABET[index]
    return cipher_text
def ceasar_decrypt(cipher_text):
    plain_text = ''
    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text +=ALPHABET[index]
    return plain_text

test = ceasar_encrypt('Welcome to my udemy course')
print(test)
plain = ceasar_decrypt(test)
print(plain)
