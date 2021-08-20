import string
import re
 


def decrypt(key, message):
    alpha = string.ascii_uppercase # quicker way of expressing the alphabet
    result = ""
    re.sub(r"X", '.', result)
    for letter in message:        
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
    return result

#A python program to illustrate Caesar Cipher Technique
def encrypt(final,s):
    result = ""
 
    # traverse text
    for i in range(len(final)):
        char = final[i] 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65) 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97) 
    return result

def clean(str):
    uppertext = unclean.upper() #convert any lowercase characters to uppercase
    nodots = re.sub(r'\.', "X", uppertext) #substitute any dots (periods) with a capital X
    nospa = re.sub(r' ', "", nodots) #substitute any occurances of spaces with no character
    final = re.sub('[^A-Za-z]+', '', nospa) #replace any numbers with no character
    return final #returns the modules output

#API for inputting user functions
   
inp = input("Would you like to encrypt or decrypt text? e or d: "); #user inputs a letter to signify whether they want to encrypt or decrypt a message
    
if inp == ('e'):
    unclean = input("Text to Encrypt: ");
    final = clean(unclean)
    s = int(input("Enter a Shift: "));
    print("Cleaned Input  : " , final);
    print("Shift : " + str(s));
    print("Cipher: " + encrypt(final,s));
    
    
elif inp == ('d'):
    unclean = input("Please enter a message to decrypt: >")
    key = int(input("Please enter a shift value or key: >:"))
    message = clean(unclean)
    plain = decrypt(key, message)
    print("Your decrypted message is: ", plain)
        
        
elif (inp != 'e' or 'd'):
    print('Your input in invalid or an error occured\nPlease try again!');
        
    
