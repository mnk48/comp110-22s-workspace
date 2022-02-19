"""EX05 - defining functions to modify lists."""

__author__ = "730389267"


def only_evens(input: list[int]) -> list[int]:
    """Returns a list of only the even integers from a given list."""
    even_list: list[int] = list()
    i: int = 0
    while i < len(input):
        if ((input[i] // 2) * 2 + 1) == (input[i] + 1):
            even_list.append(input[i])
        i += 1
    return even_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Returns a list of only the integers starting with a given start index and ending with the last integer before the given ending index of a list."""
    sub_list: list[int] = list()
    if (len(input) == 0) or (start > len(input)) or (end <= 0):
        return sub_list
    if start < 0:
        start = 0
    if end > len(input) + 1:
        end = (len(input) + 3)
    i: int = 0
    while i < (end - 1):
        sub_list.append(input[start + i])
        i += 1
    return sub_list