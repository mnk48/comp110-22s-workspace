"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730389267"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of the Node at the given index, or raises and IndexError if this index does not exist."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        i: int = 0
        if index == i:
            return head.data
        else:
            return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Given a Node, returns the maximum data value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    else:
        next: Optional[Node] = head.next
        if next is None:
            return head.data
        else:
            if next.next is None:
                if head.data < next.data:
                    return next.data
                else:
                    return head.data
            else: 
                maximum: int = head.data
                if maximum < next.data:
                    maximum = max(next)
                return maximum
    

def linkify(items: list[int]) -> Optional[Node]:
    """Creates a linked-list from a list of integers."""
    output: Node
    if len(items) == 0:
        return None
    else:
        output: Node = Node(items[0], None)
        if len(items) != 1:
            items.pop(0)
            output.next = linkify(items)
        else:
            return output
        return output
    

def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Creates a new linked list from a previous linked list by scaling each Node data by a factor."""
    if head is None:
        return None
    else:
        output: Node = Node(head.data * factor, None)
        if head.next is None:
            return output
        else:
            output.next = scale(head.next, factor)
            return output