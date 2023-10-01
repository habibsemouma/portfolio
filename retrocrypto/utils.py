from PIL import Image
alphanum = "abcdefghijklmnopqrstuvwxyz"
inverted_alphanum = alphanum[::-1]
import numpy as np
import random

secret_table = {
    'a': 39,
    'b': 86,
    'c': 72,
    'd': 63,
    'e': 54,
    'f': 98,
    'g': 42,
    'h': 23,
    'i': 57,
    'j': 113,
    'k': 207,
    'l': 131,
    'm': 172,
    'n': 94,
    'o': 67,
    'p': 122,
    'q': 76,
    'r': 111,
    's': 27,
    't': 73,
    'u': 142,
    'v': 81,
    'w': 194,
    'x': 129,
    'y': 48,
    'z': 89,
    'A': 36,
    'B': 69,
    'C': 93,
    'D': 184,
    'E': 138,
    'F': 92,
    'G': 18,
    'H': 52,
    'I': 66,
    'J': 107,
    'K': 212,
    'L': 148,
    'M': 208,
    'N': 196,
    'O': 173,
    'P': 161,
    'Q': 97,
    'R': 62,
    'S': 84,
    'T': 122,
    'U': 34,
    'V': 171,
    'W': 128,
    'X': 201,
    'Y': 117,
    'Z': 137,
    ' ': 32,
}
secret_table_reverse = {
    39: 'a',
    86: 'b',
    72: 'c',
    63: 'd',
    54: 'e',
    98: 'f',
    42: 'g',
    23: 'h',
    57: 'i',
    113: 'j',
    207: 'k',
    131: 'l',
    172: 'm',
    94: 'n',
    67: 'o',
    122: 'p',
    76: 'q',
    111: 'r',
    27: 's',
    73: 't',
    142: 'u',
    81: 'v',
    194: 'w',
    129: 'x',
    48: 'y',
    89: 'z',
    36: 'A',
    69: 'B',
    93: 'C',
    184: 'D',
    138: 'E',
    92: 'F',
    18: 'G',
    52: 'H',
    66: 'I',
    107: 'J',
    212: 'K',
    148: 'L',
    208: 'M',
    196: 'N',
    173: 'O',
    161: 'P',
    97: 'Q',
    62: 'R',
    84: 'S',
    34: 'T',
    171: 'U',
    128: 'V',
    201: 'W',
    117: 'Y',
    137: 'Z',
    32: ' ',
}

def convert_to_5x(value):
    return np.ceil(value / 5) * 5

def process_image(img):
    result=np.vectorize(convert_to_5x)(img)
    return result

def get_windows(img):
    org_dimensions=img.shape
    reshaped_img=img.flatten()
    vec_size=reshaped_img.shape[0]
    filling=25-(vec_size%25)
    pre_vector=np.concatenate([reshaped_img,np.arange(filling)],axis=0)
    windows=np.split(pre_vector,len(pre_vector)/25)
    return org_dimensions,filling, windows


def embed_text(plaintext,img):
    img=np.array(img)
    processed_img=process_image(img)
    org_dimensions,filling,windows=get_windows(processed_img)
    
    plaintext='i love cheese'
    if len(windows)<(len(plaintext)-filling):
        raise Exception('Image too small or text too short')
    for letter,window in zip(plaintext,windows):
        random_index = random.randint(0, 24)
        window[random_index]=secret_table[letter]

    restored_img=np.array(windows).flatten().astype(np.uint8)[0:-filling].reshape(org_dimensions)
    return Image.fromarray(restored_img)


def extract_text(img):
    plaintext=""
    img=np.array(img)
    org_dimensions,filling,windows=get_windows(img)
    for window in windows:
        for value in window:
            if value%5!=0:
                plaintext+=secret_table_reverse[value]
                break
    return(plaintext)


def atbash_encode(plaintext):
    plaintext = plaintext.lower()
    cipher = ""
    for letter in plaintext:
        if letter.isalpha():
            encoded_letter = inverted_alphanum[alphanum.index(letter)]
        else:
            encoded_letter = letter
        cipher += encoded_letter

    return cipher


def atbash_decode(cipher):
    cipher = cipher.lower()
    plaintext = ""
    for letter in cipher:
        if letter.isalpha():
            decoded_letter = alphanum[inverted_alphanum.index(letter)]
        else:
            decoded_letter = letter
        plaintext += decoded_letter

    return plaintext


def caesar_encode(plaintext, shift):
    plaintext = plaintext.lower()
    cipher = ""
    for letter in plaintext:
        if letter.isalpha():
            encoded_letter = alphanum[(alphanum.index(letter) + shift) % 25]
        else:
            encoded_letter = letter
        cipher += encoded_letter
    return cipher


def caesar_decode(cipher, shift):
    cipher = cipher.lower()
    plaintext = ""
    for letter in cipher:
        if letter.isalpha():
            decoded_letter = alphanum[(alphanum.index(letter) - shift) % 25]
        else:
            decoded_letter = letter
        plaintext += decoded_letter
    return plaintext


def railfence_encode(plaintext, rails):
    rail = [["\n" for i in range(len(plaintext))] for j in range(rails)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(plaintext)):
        if (row == 0) or (row == rails - 1):
            dir_down = not dir_down

        rail[row][col] = plaintext[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(rails):
        for j in range(len(plaintext)):
            if rail[i][j] != "\n":
                result.append(rail[i][j])
    return "".join(result)


def railfence_decode(cipher, rails):
    rail = [["\n" for i in range(len(cipher))] for j in range(rails)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False

        rail[row][col] = "*"
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if (rail[i][j] == "*") and (index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False

        if rail[row][col] != "*":
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


def vigenere_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def vigenere_encode(plaintext, keyword):
    key = vigenere_key(plaintext, keyword)
    cipher = []
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord("a") if plaintext[i].islower() else ord("A")
            x = (ord(plaintext[i]) - shift + ord(key[i]) - shift) % 26
            x += shift
            cipher.append(chr(x))
        else:
            cipher.append(plaintext[i])
    return "".join(cipher)


def vigenere_decode(cipher, keyword):
    key = vigenere_key(cipher, keyword)
    orig_text = []
    for i in range(len(cipher)):
        if cipher[i].isalpha():
            shift = ord("a") if cipher[i].islower() else ord("A")
            x = (ord(cipher[i]) - shift - (ord(key[i]) - shift)) % 26
            x += shift
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher[i])
    return "".join(orig_text)



