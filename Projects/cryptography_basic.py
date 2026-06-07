#revision encryption and decryption

import random 
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
#why when I assigned shuffled value to key it returns none
#key = random.shuffle(key)
random.shuffle(key)

#encryption 

plain_text = str(input("What secret message would you like to encrypt: "))
encrypted_text = ""
for letter in plain_text:
    index = chars.index(letter)
    encrypted_text += key[index]

print(f"Your encrypted text: {encrypted_text}")

#decryption 

dichiper_text = str(input("what message would you like to dichiper: "))
decrpted_text = ""
for letter in dichiper_text:
    index = key.index(letter)
    decrpted_text += chars[index]

print(f"Your decrypted text: {decrpted_text}")