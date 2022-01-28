"""EX02 - One-Shot Wordle."""

__author__ = "730389267"

secret_word: str = "python"
length: int = len(secret_word)

guess: str = input(f"What is your {length}-letter guess? ")
i: int = 0  # This variable is being established to close the loop.
index: int = 0  # This variable is being established to count the indices of the words.
emoji: str = "" 
WHITE_BOX: str = "\U00002B1C"  # These three variabels are being established to produce emojis.
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while i == 0:
    if len(guess) != length:
        guess = input(f"That was not {length} letters! Try again: ")
    else:
        while index < length:
            if guess[index] == secret_word[index]:  # If the characters at the indexes match, a green box will be added to the string.
                emoji += GREEN_BOX
            else:  # If the characters at the indexes do not match...
                character_in_guess: bool = False
                index_secret_word: int = 0
                while index_secret_word < length and character_in_guess is not True:
                    if guess[index] == secret_word[index_secret_word]:  # On the first index, this will not be true.
                        character_in_guess = True
                        emoji += YELLOW_BOX
                    else:  # We move on to check if the character is guess is the same as the next character in the secret word.
                        index_secret_word += 1
                if character_in_guess is not True:  # At the end of the loop, then all of the characters have been evaluated, and the character in guess is not in the secret word.
                    emoji += WHITE_BOX
            index += 1  # We increase the index by one to check the next character. 
        if guess == secret_word:
            print(emoji)
            print("Woo! You got it!")
            i += 1
        else:
            print(emoji)
            print("Not quite. Play again soon!")
            i += 1