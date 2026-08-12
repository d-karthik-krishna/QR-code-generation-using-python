import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

#print(chars)

chars = list(chars)
keys= chars.copy()

random.shuffle(keys)

#print(f"chars : {chars}\n keys: {keys}")

#encryption
text = input("Enter something: ")
encryption = ""

for letter in text:
    index = chars.index(letter)
    encryption += keys[index]
    
print(f"Encrypted message : {encryption}")

#decryption
text = ""
decryption = input("Enter some symbols to decrypt : ")
for symbol in decryption: 
    index = keys.index(symbol)
    text += chars[index]
    
print(f"Encrypted message : {text}")