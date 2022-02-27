"""Tests for EX06 - Dictionary Functions."""

__author__ = "730389267"

from exercises.ex06.dictionary import invert, favorite_color, count
import pytest


def test_invert_use_1() -> None:
    """Tests a regular use case for the invert function."""
    input = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(input) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use_2() -> None:
    """Tests a second regular use case for the invert function."""
    input = {'hello': 'world'}
    assert invert(input) == {'world': 'hello'}


def test_invert_edge() -> None:
    """Tests an edge use case for the invert function."""
    input = {}
    assert invert(input) == {}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_favorite_color_use_1() -> None:
    """Tests a regular use case for the favorite color function."""
    input = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(input) == "blue"


def test_favorite_color_use_2() -> None:
    """Tests a second regular use case for the favorite color function."""
    input = {"Kacey": "blue", "Malak": "green", "John": "green", "Kyra": "green", "Samia": "yellow"}
    assert favorite_color(input) == "green"


def test_favorite_color_edge_1() -> None:
    """Tests an edge case for the favorite color function when two colors are tied for favorite."""
    input = {"Malak": "blue", "John": "red", "Lorelai": "blue", "Lila": "red"}
    assert favorite_color(input) == "blue"


def test_favorite_color_edge_2() -> None:
    """Tests another edge case for the favorite color function when two colors are tied for favorite."""
    input = {"Malak": "green", "Will": "blue", "Lila": "purple", "John": "green", "Kacey": "purple", "Addison": "blue"}
    assert favorite_color(input) == "green"


def test_count_use_1() -> None:
    """Tests a regular use case for the count function."""
    xs: list[str] = ["hello", "cow", "hello", "dog"]
    assert count(xs) == {"hello": 2, "cow": 1, "dog": 1}


def test_count_use_2() -> None:
    """Tests another regular use case for the count function."""
    xs: list[str] = ["Kris", "Kris", "Kris", "Jordan"]
    assert count(xs) == {"Kris": 3, "Jordan": 1}


def test_count_edge_1() -> None:
    """Tests an edge case for the count function."""
    xs: list[str] = []
    assert count(xs) == {}