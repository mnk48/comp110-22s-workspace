"""Dictionary related utility functions for EX08."""

__author__ = "730389267"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Given a column-based table, returns a new table with only the first N rows of data."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        column_values: list[str] = []
        i: int = 0
        while i < N:
            column_values.append(column_table[column][i])
            i += 1
        result[column] = column_values
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Given a column-based table, returns a new table with only the specified columns."""
    result: dict[str, list[str]] = {}
    for name in column_names:
        result[name] = column_table[name]
    return result


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Given two column-based tables, creates a new table combining them."""
    result: dict[str, list[str]] = {}
    for column in column_table_1:
        result[column] = column_table_1[column]
    for column in column_table_2:
        if column in result:
            result[column] += column_table_2[column]
        else:
            result[column] = column_table_2[column]
    return result


def count(input: list[str]) -> dict[str, int]:
    """Given an inputed list, returns a dictionary which stores the frequency of each value within the list."""
    result: dict[str, int] = {}
    for value in input:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result


def count_ints(input: list[int]) -> dict[int, int]:
    """Given an inputed list of integers, returns a dictionary which stores the frequency of each value within the list."""
    result: dict[int, int] = {}
    i: int = 0 
    while i < len(input):
        if input[i] in result:
            result[input[i]] += 1
        else:
            result[input[i]] = 1
        i += 1
    return result


def threshold(input: dict[str, list[int]], value: int, name: list[str]) -> dict[str, list[int]]:
    """Given a column-oriented table, a threshold value, and a list of column names, creates a new table with values that are equal to or above the threshold value in the columns specified."""
    result: dict[str, list[int]] = {}
    for key in input:
        if key in name:
            i: int = 0
            j: list[int] = []
            while i < len(input[key]):
                if input[key][i] >= value:
                    j.append(input[key][i])
                i += 1
            result[key] = j
        else:
            x: list[int] = []
            i: int = 0
            while i < len(input[key]):
                x.append(input[key][i])
                i += 1
            result[key] = x
    return result


def make_int(input: dict[str, list[str]]) -> dict[str, list[int]]:
    """Turns string values into integer values in a column-oriented table."""
    result: dict[str, list[int]] = {}
    for key in input:
        i: int = 0
        j: list[int] = []
        while i < len(input[key]):
            if input[key][i] != "":
                j.append(int(input[key][i]))
            i += 1
        result[key] = j
    return result