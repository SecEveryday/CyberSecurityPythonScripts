ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def crack_ceasar(cipher_text):
    for key in range(len(ALPHABET)):
        plain_text = ''

        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index-key) % len(ALPHABET)
            plain_text += ALPHABET[index]
        print(plain_text)
crack_ceasar('ZHOFRPHCWRCPACXGHPACFRXUVH')
input()
