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
                                                                                                                                                                                                                                                                          
               AAA                                                                000000000          000000000             66666666   
              A:::A                                                             00:::::::::00      00:::::::::00          6::::::6    
             A:::::A                                                          00:::::::::::::00  00:::::::::::::00       6::::::6     
            A:::::::A                                                        0:::::::000:::::::00:::::::000:::::::0     6::::::6      
           A:::::::::A              mmmmmmm    mmmmmmm   rrrrr   rrrrrrrrr   0::::::0   0::::::00::::::0   0::::::0    6::::::6       
          A:::::A:::::A           mm:::::::m  m:::::::mm r::::rrr:::::::::r  0:::::0     0:::::00:::::0     0:::::0   6::::::6        
         A:::::A A:::::A         m::::::::::mm::::::::::mr:::::::::::::::::r 0:::::0     0:::::00:::::0     0:::::0  6::::::6         
        A:::::A   A:::::A        m::::::::::::::::::::::mrr::::::rrrrr::::::r0:::::0 000 0:::::00:::::0 000 0:::::0 6::::::::66666    
       A:::::A     A:::::A       m:::::mmm::::::mmm:::::m r:::::r     r:::::r0:::::0 000 0:::::00:::::0 000 0:::::06::::::::::::::66  
      A:::::AAAAAAAAA:::::A      m::::m   m::::m   m::::m r:::::r     rrrrrrr0:::::0     0:::::00:::::0     0:::::06::::::66666:::::6 
     A:::::::::::::::::::::A     m::::m   m::::m   m::::m r:::::r            0:::::0     0:::::00:::::0     0:::::06:::::6     6:::::6
    A:::::AAAAAAAAAAAAA:::::A    m::::m   m::::m   m::::m r:::::r            0::::::0   0::::::00::::::0   0::::::06:::::6     6:::::6
   A:::::A             A:::::A   m::::m   m::::m   m::::m r:::::r            0:::::::000:::::::00:::::::000:::::::06::::::66666::::::6
  A:::::A               A:::::A  m::::m   m::::m   m::::m r:::::r             00:::::::::::::00  00:::::::::::::00  66:::::::::::::66 
 A:::::A                 A:::::A m::::m   m::::m   m::::m r:::::r               00:::::::::00      00:::::::::00      66:::::::::66   
AAAAAAA                   AAAAAAAmmmmmm   mmmmmm   mmmmmm rrrrrrr                 000000000          000000000          666666666     


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
        print("3) Joke ")
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
        plainText = input(r"your text you want to encrypt : ")
        secretKey = input(r"enter your secretKey must be at least four unique letters/digits  : ")
    plainText = plainText.upper()
    secretKey = secretKey.upper()
    unique_chars = list(set(secretKey))
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
    for c in plainText:
        if c == " ":
            cypherText += space
        else: 
            cypherText += myCyberGuid[c] + betweenLetters
        
    
    print(cypherText)


def decrypt(cypherText = None , secretKey =None):
    if cypherText == None and secretKey == None :
        cypherText = input(r"your text you want to decrypt : ")
        secretKey = input(r"enter your secretKey must be at least four unique letters/digits  : ")
    cypherText = cypherText.upper()
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
    retries = 3
    while retries > 0:
        try:
            response = requests.get('https://v2.jokeapi.dev/joke/Programming')
            response.raise_for_status()  # raise an exception for 4xx and 5xx errors
            joke = response.json()
            if response.ok:
                return joke['joke']
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            retries -= 1
    print("Failed to get a joke after 3 retries.")
    #return None
    
    jokes = [
    "Why did the programmer encrypt his messages? He wanted to keep them on the cipher side!",
    "Why did the encryption algorithm go to the bar? It needed a byte to drink!",
    "Why did the decryption function refuse to work? It had trust issues!",
    "Why did the programmer use a Caesar cipher? He wanted to keep the message in Roman code!",
    "What do you call an encrypted message that's difficult to decode? A hard cipher!"
    ]
    random_no = random.randint(0,4)
    return jokes[random_no]



if __name__== '__main__':
    try:
        fire.Fire(home)
    except KeyboardInterrupt:
        print("\nleaving !!")
    
