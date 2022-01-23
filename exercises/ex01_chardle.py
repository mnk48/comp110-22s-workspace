"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730389267"    

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a single character")
    exit()

instance: int = 0
print("Searching for " + character + " in " + word)

if word[0] == character:
    print(character + " found at index 0")
    instance = instance + 1
if word[1] == character:
    print(character + " found at index 1")
    instance = instance + 1
if word[2] == character:
    print(character + " found at index 2")
    instance = instance + 1
if word[3] == character:
    print(character + " found at index 3")
    instance = instance + 1
if word[4] == character:
    print(character + " found at index 4")
    instance = instance + 1 

if instance == 0: 
    print("No instances of " + character + " found in " + word)
else:    
    if instance == 1:
        print("1 instance of " + character + " found in " + word)
    else:
        if instance == 2:
            print("2 instances of " + character + " found in " + word)
        else:
            if instance == 3:
                print("3 instances of " + character + " found in " + word)
            else:
                if instance == 4:
                    print("4 instances of " + character + " found in " + word)
                else:
                    if instance == 5:
                        print("5 instances of " + character + " found in " + word)