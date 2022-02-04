"""EX03 - Structured Wordle."""

__author__ = "730389367"

WHITE_BOX: str = "\U00002B1C"  
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool:
    """Searches for character in word."""
    assert len(character) == 1
    i: int = 0
    character_in_word: bool = False
    while i < len(word):
        if character == word[i]:  # If the character is in both words at the same index...
            character_in_word = True  # Then the character is in the word.
            i += 1
        else:  # If not, move on to the next index. 
            i += 1
    if character_in_word is True:
        return True
    else:
        return False 


def emojified(guess: str, secret: str) -> str:
    """Emojifies guess in comparison to secret."""
    assert len(guess) == len(secret)
    emoji: str = ""
    j: int = 0
    while j < len(secret):
        if contains_char(secret, guess[j]) is False:  # If the character at index j of the guess is not in secret, emojify it by adding a white box.
            emoji += WHITE_BOX
            j += 1
        else: 
            if guess[j] == secret[j]:  # If the character in guess is in secret, and they are at the same index, emojify it by adding a green box.
                emoji += GREEN_BOX
                j += 1
            else:  # If the character in guess is in secret, but not at the same index, emojify it by adding a yellow box.
                emoji += YELLOW_BOX
                j += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Ensures guess is the same as the expected length of secret."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    idx: int = 0
    while idx == 0:
        if len(guess) == expected_length:  # If the length of the guess is the same as the length of the secret word, return the guess.
            return guess
        else:
            guess = input(f"That was not {expected_length} letters! Try again: ")  # If not, promopt the user for another word.


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    win: bool = False
    while turn <= 6 and win is False:
        print(f"=== Turn {turn}/6 ===")
        official_guess: str = input_guess(len(secret_word))  # The official guess is a result of the input_guess function testing if it is the correct length.
        print(emojified(official_guess, secret_word))  # The emojified function determines what characters in the official guess are in the secret word, and at what indices.
        if emojified(official_guess, secret_word) == len(secret_word) * GREEN_BOX:  # If emojified produces as many green boxes as the length of the word, the user wins.
            win = True
        else:  # If not, the game moves to the next turn. 
            turn += 1
    if win is True:  # If by the end of the loop, win is true, then print... 
        print(f"You won in {turn}/6 turns!")
    else:  # If by the end of the loop, win is not true, then print... 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()