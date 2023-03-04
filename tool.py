import fire
import string 
import random
main = list(string.ascii_uppercase + string.digits + string.punctuation)

def home(plainText=None,secretKey=None,cypherText=None):

    if plainText == None and secretKey == None and  cypherText == None :
        import time

        logo = '''
        .------..------..------..------..------..------.
        |A.--. ||M.--. ||R.--. ||0.--. ||0.--. ||6.--. |
        | (\/) || (\/) || :(): || :/\: || :/\: || (\/) |
        | :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
        | '--'A|| '--'M|| '--'R|| '--'0|| '--'0|| '--'6|
        `------'`------'`------'`------'`------'`------'
        '''

        lines = logo.split('\n')

        # Remove empty lines from the end of the logo
        while not lines[-1]:
            lines.pop()

        # Calculate the length of the longest line
        max_line_length = max(len(line) for line in lines)

        # Add padding to the end of shorter lines
        for i in range(len(lines)):
            lines[i] += ' ' * (max_line_length - len(lines[i]))

        # Print the logo line by line with a delay
        for line in lines:
            print(line)
            time.sleep(0.2)  # Add a 0.1 second delay between each line

        print("1) Encrypt ")
        print("2) Decrypt ")
        print("3) Joke ")
        choice = input("Make your choice by numbers 1 --> 3 !!!")

        if choice == "1":
            encrypt()
        elif choice == "2":
            decrypt()
        else:
            joke()
    elif plainText != None and secretKey != None :
        print("enc")
        encrypt(plainText,secretKey)
    elif cypherText != None and secretKey != None :
        decrypt(cypherText,secretKey)
    else:
        print("Something Went Worng !!")
    



def encrypt(plainText=None,secretKey=None):
    if plainText == None and secretKey == None :
        plainText = input("your text you want to encrypt : ").upper()
        secretKey = input("enter your secretKey must be at least four unique letters/digits  : ").upper()
    plainText.upper()
    secretKey.upper()
    unique_chars = list(set(secretKey.upper()))
    unique_chars.sort()
    space = unique_chars[-1]
    betweenLetters = unique_chars[-2]
    unique_chars = unique_chars[:-2]
    #print(unique_chars)
    numberOfUniqueSecretKeyLetters = len(unique_chars)
    plainTextCharacters = plainText.replace(" ","")
    plainTextCharacters = list("".join(plainTextCharacters.upper()))
    
    #print(plainTextCharacters)
    #numberOfUniquePlainTextLetters = len(plainTextCharacters)
    hold = len(main) / numberOfUniqueSecretKeyLetters
    if not hold.is_integer():
        hold = int(hold) + 1 
    myCyberGuid = {}
    #print(hold)
    cn = 1 
    index = 0 
    for c in main : 
        if cn % (hold+1) == 0 :
            index += 1 
            cn = 1
        
        myCyberGuid[c] = cn * unique_chars[index]
        cn += 1
    
    #print(myCyberGuid)

    cypherText = ""
    for c in plainText.upper():
        if c == " ":
            cypherText += space
        else: 
            cypherText += myCyberGuid[c] + betweenLetters
        
    
    print(cypherText)


def decrypt(cypherText = None , secretKey =None):
    if cypherText == None and secretKey == None :
        cypherText = input("your text you want to decrypt : ").upper()
        secretKey = input("enter your secretKey must be at least four unique letters/digits  : ").upper()
    cypherText.upper()
    secretKey.upper()
    unique_chars = list(set(secretKey.upper()))
    unique_chars.sort()
    space = unique_chars[-1]
    betweenLetters = unique_chars[-2]
    unique_chars = unique_chars[:-2]
    #print(unique_chars)
    numberOfUniqueSecretKeyLetters = len(unique_chars)
    cypherTextCharacters = cypherText.replace(" ","")
    cypherTextCharacters = list("".join(cypherTextCharacters))
    
    #print(cypherTextCharacters)
    #numberOfUniquecypherTextLetters = len(cypherTextCharacters)
    hold = len(main) / numberOfUniqueSecretKeyLetters
    if not hold.is_integer():
        hold = int(hold) + 1 
    myCyberGuid = {}
    #print(hold)
    cn = 1 
    index = 0 
    for c in main : 
        if cn % (hold+1) == 0 :
            index += 1 
            cn = 1
        
        myCyberGuid[cn * unique_chars[index]] = c 
        cn += 1
    
    #print(myCyberGuid)

    plainText = ""
    temp = ""
    for c in cypherText:
        if c == space:
            plainText += " "
        elif c == betweenLetters: 
            plainText += myCyberGuid[temp] 
            temp = ""
        else:
            temp += c
        
        #print(temp)
    
    print(plainText)



def joke():
    jokes = [
    "Why did the programmer encrypt his messages? He wanted to keep them on the cipher side!",
    "Why did the encryption algorithm go to the bar? It needed a byte to drink!",
    "Why did the decryption function refuse to work? It had trust issues!",
    "Why did the programmer use a Caesar cipher? He wanted to keep the message in Roman code!",
    "What do you call an encrypted message that's difficult to decode? A hard cipher!"
    ]
    random_no = random.randint(0,4)
    print(jokes[random_no])



if __name__== '__main__':
    fire.Fire(home)

    
