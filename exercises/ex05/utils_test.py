"""EX05 - tests for only_evens, sub, and concat."""

__author__ = "730389267"


from exercises.ex05.utils import only_evens, sub


def test_only_evens_use_1() -> None:
    """Tests the only_evens function to see if a list of only even integers is generated."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_use_2() -> None:
    """Tests the only_evens function to see if another list of only even integers is generated."""
    xs: list[int] = [22, 44, 45, 1000, 32, 56, 56, 99]
    assert only_evens(xs) == [22, 44, 1000, 32, 56, 56]


def test_only_evens_edge() -> None:
    """Tests an edge case for the only_evens function."""
    xs: list[int] = [-4, -6, -1000, 0, 1, -56]
    assert only_evens(xs) == [-4, -6, -1000, 0, -56]


def test_sub_use_1() -> None:
    """Tests a use case for the sub function."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_edge() -> None:
    """Tests an edge case for the sub function."""
    xs: list[int] = [-3, 4, 5, -7]
    assert sub(xs, -2, 4) == [-3, 4, 5, -7]