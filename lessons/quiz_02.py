"""Practice making functions for QZ02."""


def odd_and_even(input: list[int]) -> list[int]:
    """Given an inputed list, returns a list of the values that are odd and at even indices."""
    xs: list[int] = []
    i: int = 0
    while i < len(input):
        if input[1] % 2 == 1 and i % 2 == 0:
            xs.append(input[i])
        i += 1
    return xs


def vowels_and_threes(input: str) -> str:
    """Given a string, returns a new string containing the characters that are at an index of multiple 3 or a vowel."""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    weird: str = "" 
    i: int = 0
    while i < len(input):
        if input[i] in vowels:
            if i % 3 != 0 and i != 0:
                weird += input[i]
        else:
            if i % 3 == 0 or i == 0:
                weird += input[i]
        i += 1
    return weird 


def average_grades(input: dict[str, list[int]]) -> dict[str, float]:
    """Calculates an average grade for each student."""
    gradebook: dict[str, float] = {}
    for name in input:
        total: float = 0
        for grade in input[name]:
            total += grade
        total = total / len(input[name])
        gradebook[name] = total
    return gradebook
