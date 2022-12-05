from caesar_cipher.corpus_loader import word_list, name_list

# Create an encrypt function that takes in a plain text phrase
# and a numeric shift.
# the phrase will then be shifted that many letters.
# E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10)
# would return ‘klm’.
# shifts that exceed 26 should wrap around.
# E.g. encrypt(‘abc’,27) would return ‘bcd’.
# shifts that push a letter out or range should wrap around.
# E.g. encrypt(‘zzz’,1) would return ‘aaa’.


def encrypt(plain_text, key):
    pass
    letter_shifted = ''
    for char in range(len(plain_text)):
        char = plain_text[char]
        if char.isupper():
            letter_shifted += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            letter_shifted += chr((ord(char) + key - 97) % 26 + 97)
        else:
            letter_shifted += char
    return letter_shifted


def decrypt(encrypted, key):
    return encrypt(encrypted, - key)
    pass


def crack(encrypt_text):
    for char in range(26):
        count = 0
        words = encrypt(encrypt_text, char)
        lst = words.split()
        for word in lst:
            if word in name_list or word.lower() in word_list:
                count += 1
        if (count / len(lst)) > .5:
            return ' '.join(lst)
    return ''


if __name__ == '__main__':
    print(encrypt(123, 1))
    print(encrypt('ABC', 7))
