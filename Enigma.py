import fire
import string 
import random
import subprocess
import requests

#subprocess.run(['pip', 'install', '-r', 'requirements.txt'])



main = list(string.ascii_uppercase + string.digits + string.punctuation)

def home(plainText=None,secretKey=None,cypherText=None):

    if plainText == None and secretKey == None and  cypherText == None :
        import time

        logo = '''
           
 █████╗ ███╗   ███╗██████╗  ██████╗  ██████╗  ██████╗ 
██╔══██╗████╗ ████║██╔══██╗██╔═████╗██╔═████╗██╔════╝ 
███████║██╔████╔██║██████╔╝██║██╔██║██║██╔██║███████╗ 
██╔══██║██║╚██╔╝██║██╔══██╗████╔╝██║████╔╝██║██╔═══██╗
██║  ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ 
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
            time.sleep(0.1)  # Add a 0.1 second delay between each line

        print("1) Encrypt ")
        print("2) Decrypt ")
        print("3) Joke :) ")
        choice = input("Make your choice by numbers 1 --> 3 : ")

        if choice == "1":
            encrypt()
        elif choice == "2":
            decrypt()
        elif choice == "3":
            print(joke())
        else:
            print("That's not an Option ! ")

    elif plainText != None and secretKey != None :
        #print("enc")
        encrypt(plainText,secretKey)
    elif cypherText != None and secretKey != None :
        decrypt(cypherText,secretKey)
    else:
        print("Something Went Worng !!")
    



def encrypt(plainText=None,secretKey=None):
    if plainText == None and secretKey == None :
        plainText = str(input(r"your text you want to encrypt : "))
        secretKey = str(input(r"Your secret key : "))
    plainText = str(plainText)
    print(plainText)
    secretKey = str(secretKey).replace(" ","") #to remove spaces
    unique_chars = list(set(secretKey))
    while len(unique_chars) < 3:
        print(r"**Your secret key must have at least 3 unique characters/digits/symbols**")
        secretKey = input(r"Your secret key : ")
        secretKey = secretKey.replace(" ","") 
        unique_chars = list(set(secretKey))
        
    
    secretKey = secretKey.upper()
    unique_chars.sort()
    space = unique_chars[-1]
    betweenLetters = unique_chars[-2]
    unique_chars = unique_chars[:-2] 
    #print(unique_chars)
    numberOfUniqueSecretKeyLetters = len(unique_chars)
    plainTextCharacters = plainText.replace(" ","") #to remove spaces 
    plainTextCharacters = list("".join(plainTextCharacters))#list characters of the plaintext
    
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
    for c in plainText:
        if c == " ":
            cypherText += space
        else: 
            if c.isupper():
                cypherText +='~' + myCyberGuid[c.upper()] + betweenLetters
            else:
                cypherText += myCyberGuid[c.upper()] + betweenLetters
    
    print("Your encrypted message : " + cypherText)


def decrypt(cypherText = None , secretKey =None):
    if cypherText == None and secretKey == None :
        cypherText = str(input(r"Your text you want to decrypt : "))
        secretKey = str(input(r"Your secret key : "))
    cypherText = str(cypherText).upper()
    secretKey = str(secretKey).replace(" ","") #to remove spaces
    secretKey = secretKey.upper()
    unique_chars = list(set(secretKey))
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
    cap = False
    for c in cypherText:
        if c == '~':
            cap = True
        elif c == space:
            plainText += " "
        elif c == betweenLetters: 
            if cap == True:
                plainText += myCyberGuid[temp]
                temp = ""
                cap = False
            else:
                plainText += myCyberGuid[temp].lower()
                temp = ""
        else:
            temp += c
        
        #print(temp)
    
    print("Your secret message : " + plainText)



def joke():
    #list of jokes for backup if the API didnt work or no internet :)
    jokes = [
    "Why did the programmer encrypt his messages? He wanted to keep them on the cipher side!",
    "Why did the encryption algorithm go to the bar? It needed a byte to drink!",
    "Why did the decryption function refuse to work? It had trust issues!",
    "Why did the programmer use a Caesar cipher? He wanted to keep the message in Roman code!",
    "What do you call an encrypted message that's difficult to decode? A hard cipher!"
    ] 

    random_no = random.randint(0,4)
    retries = 3
    while retries > 0:
        try:
            response = requests.get('https://v2.jokeapi.dev/joke/Programming')
            response.raise_for_status()  # raise an exception for 4xx and 5xx errors
            joke = response.json()
            if 'joke' in joke:
                return joke['joke']
            elif retries > 0:
                retries -= 1
            else:
                return jokes[random_no]
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            retries -= 1
    print("Failed to get a joke after 3 retries.")
    #return None
    
    
    
    



if __name__== '__main__':
    try:
        fire.Fire(home)
    except KeyboardInterrupt:
        print("\nleaving !!")
    
