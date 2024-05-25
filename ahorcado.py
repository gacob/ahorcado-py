#
# Exercise: Ahorcado game
# Basically a random word gets chosen. You say a syllabe and you can get it right or wrong. After 6 wrong tries, you lose.
# 

import random

#Variables
try:
    with open("wordlist.txt", "rt") as linea:
        Lista = [line.strip() for line in linea]
except:
    print("Word List not found")
    
tries = int(6)
emptyword = []
fullword = []
        
        
# It's the one starting the game
def general():
        
    print ("Welcome to the Ahorcado!")
    print ("In this game, you have to guess what is the word in the empty sockets. You have 6 tries, good luck!")
    print ("------")
    print ("|   | ")
    print ("| ")
    print ("| ")
    print ("| ")
    print ("_________")
    
    GetaWord()
    UserInput()
    
        
    # Choose a word at random from wordlist.txt. Also:
    # 1º Store the word in Fullword for a later use
    # 2º Store the word letters in the form "_" in Emptyword
def GetaWord():
    global count
    
    listrandom = random.choice(Lista)

    for x in listrandom:
        fullword.append(x)
        emptyword.append("_")
            
    print(emptyword)
    count = len(fullword)
    
    # User introduces a syllabe and make sure it's only one and alphabetical. Then execute Checker()
def UserInput():
    global letra
    
    letra = input("Write a syllabe:")
        
    if len(letra) > 1:
        print("Please introduce only one syllabe")
        UserInput()
        
    elif not letra.isalpha():
        print("Please introduce only alphabetic letters")
        UserInput
            
    else:
        Checker()
            
            
    # Checks if the syllabe introduced is in the word and decide winner or loss
def Checker():
    global tries, count, emptyword, fullword
    
    if letra in fullword: # Righht word
        print("You got it right!")
        emptyword.pop((fullword.index(letra))) # Removes the next Emptyword's empty socket
        emptyword.insert(fullword.index(letra), letra) # Introduces the Letter in the Emptyword's empty socket
        
        fullword.insert(fullword.index(letra), "_")
        fullword.remove(letra) # Removes the Letter from the original word
        
        count = count - 1
        
        if count > 0:
            print(emptyword)
            UserInput()
            
        else:
            print(emptyword)
            print("You have won the game!")
            input()
            
    else: # Wrong word
        print("You got it wrong. You have", tries, "left")
        tries = tries - 1
            
        if tries == 5:
            print ("------")
            print ("|   | ")
            print ("|   o ")
            print ("| ")
            print ("| ")
            print ("_________")
            UserInput()
                
        elif tries == 4:
            print ("------")
            print ("|   |")
            print ("|   o")
            print ("|  /")
            print ("| ")
            print ("_________")
            UserInput()
                
        elif tries == 3:
            print ("------")
            print ("|   |")
            print ("|   o")
            print ("|  /|")
            print ("| ")
            print ("_________")
            UserInput()
                
        elif tries == 2:
            print ("------")
            print ("|   |")
            print ("|   o")
            print ("|  /|\ ")
            print ("| ")
            print ("_________")
            UserInput()
                
        elif tries == 1:
            print ("------")
            print ("|   |")
            print ("|   o")
            print ("|  /|\ ")
            print ("|  /     ")
            print ("_________")
            UserInput()
                                
        else: 
            print ("------")
            print ("|   | ")
            print ("|   o ")
            print ("|  /|\ ")
            print ("|  / \ ")
            print ("_________")
            print ("Game has finished. You have lost.")
            input()
                
general()