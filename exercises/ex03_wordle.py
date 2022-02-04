"""EX03 - Structured Wordle."""

__author__ = "730389367"


def contains_char(word: str, character: str) -> bool:
    """Searches for character in word."""
    assert len(character) == 1
    i: int = 0
    character_in_word: bool = False
    while i < len(word):
        if character == word[i]:
            character_in_word = True
            i += 1
        else:
            i += 1
    if character_in_word is True:
        return True
    else:
        return False 


def emojified(guess: str, secret: str) -> str:
    """Emojifies guess in comparison to secret."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"  
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    j: int = 0
    while j < len(secret):
        if contains_char(secret, guess[j]) is False:
            emoji += WHITE_BOX
            j += 1
        else: 
            if guess[j] == secret[j]:
                emoji += GREEN_BOX
                j += 1
            else:
                emoji += YELLOW_BOX
                j += 1
    return emoji


def input_guess(expected_length: int) -> str:
    guess: str = input(f"Enter a {expected_length} character word: ")
    index: int = 0
    while index == 0:
        if len(guess) == expected_length:
            return guess
        else:
            guess = input(f"That was not {expected_length} letters! Try again: ")
            index = 0


def main