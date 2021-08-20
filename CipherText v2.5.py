#Author: Oskar Petersen
#Date: 11/08/2021

#Algorithm
#The encryption module will receive a cleaned piece of text from the clean() module
#the module will then traverse the string it receives to sort the characters into an array 
#module double checks that the array contains uppercase letters (error correction)
#module will then apply the shift value to the string
#module will then return the encrypted string 

#Encryption Module test table
#   INPUT                                         KEY          |     OUTPUT

#1  ABCDEF                                         3           |     DEFGHI                   
#2  HELLOTHERE                                    13           |     URYYBGURER               
#3  TESTTEST                                      25           |     SDRSSDRS            
#4  UNITTEST                                      25           |     TMHSSDRS     
#5  VERYLONGSTRINGOFCHARACTERSTOTESTTHEMODULE     14           |     JSFMZCBUGHFWBUCTQVOFOQHSFGHCHSGHHVSACRIZS  
#6  TESTINGTHISMODULEISKINDABORING                14           |     HSGHWBUHVWGACRIZSWGYWBROPCFWBU
#7  LMAOIKNOWTHISWORKS                             6           |     RSGUOQTUCZNOYCUXQY
#8  ONLYTHREEMORETOGO                              9           |     XWUHCQANNVXANCXPX
#9  MYANACONDADONTWANTNONE                        15           |     BNPCPRDCSPSDCILPCICDCT                      
#10 UNLESSYOUGOTBUNSHUN                           15           |     JCATHHNDJVDIQJCHWJC             



#library imports
import string #for string manipulation
import re #for substitution
import sys #for commandlind arguments and the sys.exit module
 



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

#encryption module
def encrypt(final,s):
    #variable definition to store the result of the encryption function
    result = "" 
    # traverse text and sort into an array to be shifted
    for i in range(len(final)):
        char = final[i] 
        # double checks that the string is in fact uppercase
        if (char.isupper()):
            #function to perform the cipher shift
            result += chr((ord(char) + s-65) % 26 + 65)  
    return result

#module to clean a user inputted string before it is passed along to the encrypt and decrypt module think of this module as error handling and protecting the user from themselves
def clean(str):
    uppertext = unclean.upper() #convert any lowercase characters to uppercase
    nodots = re.sub(r'\.', "X", uppertext) #substitute any dots (periods) with a capital X
    nospa = re.sub(r' ', "", nodots) #substitute any occurances of spaces with no character
    final = re.sub('[^A-Za-z]+', '', nospa) #replace any numbers with no character
    return final #returns the modules output

#allocating module to unit tests as its more efficient than writing out 10 separate unit tests with different variables
def UnitTests():
    #Inputdata contains a list of strings to run through the encrypt module as unit tests
    InputData = ['ABCDEF', 'HELLOTHERE', 'TESTTEST', 'UNITTEST' ,'VERYLONGSTRINGOFCHARACTERSTOTESTTHEMODULE', 'TESTINGTHISMODULEISKINDABORING', 'LMAOIKNOWTHISWORKS', 'ONLYTHREEMORETOGO', 'MYANACONDADONTWANTNONE', 'UNLESSYOUGOTBUNSHUN']
    Shifts = ['3', '13', '25', '25', '14', '14', '6', '9', '15', '15'] #list to store the shift values used for unit tests
    #expectdata contains the expected outputs of the encrypt module given above shift values
    Expectdata = ['DEFGHI', 'URYYBGURER', 'SDRSSDRS', 'TMHSSDRS', 'JSFMZCBUGHFWBUCTQVOFOQHSFGHCHSGHHVSACRIZS', 'HSGHWBUHVWGACRIZSWGYWBROPCFWBU', 'RSGUOQTUCZNOYCUXQY', 'XWUHCQANNVXANCXPX', 'BNPCPRDCSPSDCILPCICDCT', 'JCATHHNDJVDIQJCHWJC']
    result = [] #empty list variable to store the strings returned from the encrypt module
    count = 0 #unit test count variable
    
    #iterate across Inputdata and shifts 
    for x,y in zip(InputData, Shifts):
        result.append(encrypt(x,int(y))) #append the returned values to the results list
        
    #code for checking the returned results
    
    #iterate across the lists and check the returned results against the expected data
    #module will print out the input string, the expected data and finally the result returned from the encrypt module
    for m,n,o in zip(result, Expectdata, InputData):
        if m == n:
            print("Input String: ", o)
            print("Expected Data: ", n)
            print("Result: ", m)
            count+=1
            print("Unit Test", count, " Okay\n")
            
        else:
            print("Input String: ", o)
            print("Expected Data: ", n)
            print("Result: ", m)
            count+=1
            print("Unit Test", count ," Fail\n")
    sys.exit() #sysexit seems to help prevent an index error occuring at the end of the unit test module


#API
    
#first try and except block will check if the user is attempting to perform a unit test
#with the sys arg flag -t, if not it will pass onto the next try and except block
    
#for some reason when trying to nest the "if inp == -t" code within the same try and except block causes problems (IndexError)
#organising the code in this fashion is less efficient but it works *shrug*


try:
    inp = sys.argv[1]
    
    if inp == ('-t'):
        UnitTests()
    
except IndexError as ie:
    pass

try:
    #system arguments
    inp = sys.argv[1]
    key = int(sys.argv[2])
    s = int(sys.argv[2])
    unclean = sys.argv[3]
    
    
    if inp == ('-e') or inp == ('--encrypt'): #I wanted to allow a friendly CLI experience with the standard -$VariableChar and --$VariableString
        final = clean(unclean) #calls the clean module to remove any illegal characters that may break the program
        print("Cleaned Input  : " , final); #outputs the cleaned output for the user to see exactly what has been passed to the encryption module
        print("Shift : " + str(s)); #outputs the string for the user to note
        print("Cipher: ", encrypt(final,s));
        sys.exit()
            
    if inp == ('-d') or inp == ('--decrypt'):
        message = clean(unclean) #same as above
        plain = decrypt(key, message) #passes the string to the decryption module
        print("Your decrypted message is: ", plain)
        sys.exit()
        
    else: #error handling in case of bad input
        raise SyntaxError('Your encryption/decryption input is invalid\nPlease try again!');


except ValueError as ve: #exception for catching invalid shift values in the case of an entered letter or symbol
    print('Bummer!', ve.__class__, "occured.");
    print('The shift value must be a number');
    
except Exception as e: #exception handling, will catch the error and present it to the user in a digestable way
    print("Bummer!", e.__class__, "occurred.")
    print(e)
    pass   



        
        
    
    
