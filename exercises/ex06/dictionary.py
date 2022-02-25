"""EX06 - Dictionary Functions."""

__author__ = "730389267"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, inverts its key and value pairs."""
    inverted: dict[str, str] = dict()
    for key in dictionary:
        if dictionary[key] == key:
            raise KeyError("Can't input duplicate keys.")
        else:
            inverted[dictionary[key]] = key
    return inverted
