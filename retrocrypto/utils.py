import numpy as np
alphanum="abcdefghijklmnopqrstuvwxyz"
inverted_alphanum=alphanum[::-1]
def atbash_encode(plaintext):
    plaintext=plaintext.lower()
    cipher=""
    for letter in plaintext:
        if letter.isalpha():
            encoded_letter=inverted_alphanum[alphanum.index(letter)]
        else: encoded_letter=letter
        cipher+=encoded_letter

    return cipher

def atbash_decode(cipher):
    cipher=cipher.lower()
    plaintext=""
    for letter in cipher:
        if letter.isalpha():
            decoded_letter=alphanum[inverted_alphanum.index(letter)]
        else: decoded_letter=letter
        plaintext+=decoded_letter

    return plaintext


def caesar_encode(plaintext,shift):
    plaintext=plaintext.lower()
    cipher=""
    for letter in plaintext:
        if letter.isalpha():
            encoded_letter=alphanum[(alphanum.index(letter)+shift)%25]
        else:encoded_letter=letter
        cipher+=encoded_letter
    return cipher

def caesar_decode(cipher,shift):
    cipher=cipher.lower()
    plaintext=""
    for letter in cipher:
        if letter.isalpha():
            decoded_letter=alphanum[(alphanum.index(letter)-shift)%25]
        else:decoded_letter=letter
        plaintext+=decoded_letter
    return plaintext






def railfence_encode(plaintext, rails):

	rail = [['\n' for i in range(len(plaintext))]
				for j in range(rails)]
	
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
			if rail[i][j] != '\n':
				result.append(rail[i][j])
	return("" . join(result))
	



def railfence_decode(cipher, rails):

	rail = [['\n' for i in range(len(cipher))]
				for j in range(rails)]

	dir_down = None
	row, col = 0, 0

	for i in range(len(cipher)):
		if row == 0:
			dir_down = True
		if row == rails - 1:
			dir_down = False
		
		
		rail[row][col] = '*'
		col += 1
		
		if dir_down:
			row += 1
		else:
			row -= 1
			
	index = 0
	for i in range(rails):
		for j in range(len(cipher)):
			if ((rail[i][j] == '*') and
			(index < len(cipher))):
				rail[i][j] = cipher[index]
				index += 1
		
	result = []
	row, col = 0, 0
	for i in range(len(cipher)):

		if row == 0:
			dir_down = True
		if row == rails-1:
			dir_down = False
			
		
		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1
		
		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(result))

def vigenere_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def vigenere_encode(plaintext, keyword):
    key = vigenere_key(plaintext, keyword)
    cipher = []
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord('a') if plaintext[i].islower() else ord('A')
            x = (ord(plaintext[i]) - shift + ord(key[i]) - shift) % 26
            x += shift
            cipher.append(chr(x))
        else:
            cipher.append(plaintext[i])
    return ''.join(cipher)

def vigenere_decode(cipher, keyword):
    key = vigenere_key(cipher, keyword)
    orig_text = []
    for i in range(len(cipher)):
        if cipher[i].isalpha():
            shift = ord('a') if cipher[i].islower() else ord('A')
            x = (ord(cipher[i]) - shift - (ord(key[i]) - shift)) % 26
            x += shift
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher[i])
    return ''.join(orig_text)

