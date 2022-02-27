"""EX06 - Dictionary Functions."""

__author__ = "730389267"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, inverts its key and value pairs."""
    inverted: dict[str, str] = dict()
    for key in dictionary:
        if dictionary[key] in inverted:
            raise KeyError("Stop.")
        else:
            inverted[dictionary[key]] = key
    return inverted


def favorite_color(dictionary: dict[str, str]) -> str:
    """Given a dictionary of names and favorite colors, returns the most popular favorite color."""
    score: dict[str, int] = dict()
    winner: str = ""
    counter: int = 0
    for name in dictionary:
        score[dictionary[name]] = 0
    for name in dictionary:
        score[dictionary[name]] += 1
    for color in score:
        if score[color] > counter:
            winner = color
            counter = score[color]
    return winner


def count(input: list[str]) -> dict[str, int]:
    tally: dict[str, int] = dict()
    i: int = 0
    while i < len(input):
        if input[i] in tally:
            tally[input[i]] += 1
        else:
            tally[input[i]] = 1
        i += 1
    return tally