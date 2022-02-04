"""EX03 - Structured Wordle."""

__author__ = "730389367"


def contains_char(guess: str, character: str) -> bool:
    """Searches for character in guess."""
    assert len(character) == 1
    index: int = 0
    while index < len(guess):
        if character == guess[index]:
            return True
        else:
            index += 1
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
        if contains_char(guess, secret[j]) is True:
            emoji += GREEN_BOX
        else: 
        
    

