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
    if end > len(input):
        end = len(input)
    i: int = 0
    while i < (end - start):
        sub_list.append(input[start + i])
        i += 1
    return sub_list


def concat(first_input: list[int], second_input: list[int]) -> list[int]:
    """Creates a list of integers inputed from two seperate lists, in the order of the inputed lists."""
    concat_list: list[int] = list()
    i: int = 0
    while i < len(first_input):
        concat_list.append(first_input[i])
        i += 1
    j: int = 0
    while j < len(second_input):
        concat_list.append(second_input[j])
        j += 1
    return concat_list