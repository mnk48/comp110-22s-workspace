"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730389267"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """value_at cannot work on an empty linked list."""
    with pytest.raises(IndexError):
        value_at(None, 3)


def test_value_at_non_empty_0() -> None:
    """A non-empty linked list with a specified index of 0 should return the data of the head Node."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_value_at_non_empty_above_0() -> None:
    """A non-empty linked list should return the data value of the Node at the specified index."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 2) == 30


def test_max_at_empty() -> None:
    """max cannot work on am empty linked list."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_linkify_at_empty() -> None:
    """linkify will return None upon an empty list."""
    items: list[int] = []
    assert linkify(items) is None


def test_linkify_non_empty() -> None:
    """linkify will return a Node composed of the inputed list items in order."""
    items: list[int] = [1, 2, 3]
    assert linkify(items).__str__() == "1 -> 2 -> 3 -> None"


def test_linkify_non_empty_1() -> None:
    """linkify will return a Node composed of the inputed list items in order."""
    items: list[int] = [4, 1, 6, 7]
    assert linkify(items).__str__() == "4 -> 1 -> 6 -> 7 -> None"


def test_scale_empty() -> None:
    """scale will return an empty linked list upon the input of an empty linked list."""
    linked_list: None = None
    assert scale(linked_list, 5) is None 


def test_scale_non_empty() -> None:
    """scale will return a new linked list by returning a new linked list of the scaled data of the inputed linked list."""
    linked_list: Node = Node(1, Node(2, Node(3, None)))
    assert scale(linked_list, 2).__str__() == "2 -> 3 -> 6 -> None"