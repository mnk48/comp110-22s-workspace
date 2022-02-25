"""Tests for EX06 - Dictionary Functions."""

__author__ = "730389267"

from exercises.ex06.dictionary import invert
import pytest


def test_invert_use_1() -> None:
    """Tests a regular use case for the invert function."""
    input = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(input) == {'z': 'a', 'y': 'b', 'x': 'c'}


# def test_invert_edge() -> None:
#     """Tests an edge case for the invert function."""


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)