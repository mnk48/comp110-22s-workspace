"""EX05 - tests the only_evens, sub, and concat functions."""

__author__ = "730389267"


from exercises.ex05.utils import only_evens, sub, concat 


def test_only_evens_use_1() -> None:
    """Tests the only_evens function to see if a list of only even integers is generated."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_use_2() -> None:
    """Tests the only_evens function to see if another list of only even integers is generated."""
    xs: list[int] = [22, 44, 45, 1000, 32, 56, 56, 99]
    assert only_evens(xs) == [22, 44, 1000, 32, 56, 56]


def test_only_evens_edge_1() -> None:
    """Tests an edge case for the only_evens function - when zero is inputed."""
    xs: list[int] = [-4, -6, -1000, 0, 1, -56]
    assert only_evens(xs) == [-4, -6, -1000, 0, -56]


def test_only_evens_edge_2() -> None:
    """Tests an edge case for the only_evens function when no even numbers are inputed."""
    xs: list[int] = [-1, -3, 5, 77, 9]
    assert only_evens(xs) == []


def test_sub_use_1() -> None:
    """Tests a use case for the sub function with basic input and starting and ending indices that do not need to be reassigned."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_use_2() -> None:
    """Tests a second use case for the sub function with basic input but one index out of range."""
    xs: list[int] = [-6, 48, 48, 0, 3]
    assert sub(xs, 2, 99) == [48, 0, 3]


def test_sub_edge() -> None:
    """Tests an edge case for the sub function when the starting index is less than 0 and the ending index is greater than the length of the list."""
    xs: list[int] = [-3, 4, 5, -7]
    assert sub(xs, -2, 5) == [-3, 4, 5, -7]


def test_sub_edge_2() -> None:
    """Tests an edge case for the sub function when the inputed list is empty."""
    xs: list[int] = []
    assert sub(xs, 0, 0) == []


def test_concat_use_1() -> None:
    """Tests a regular use case for the concat function."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_use_2() -> None:
    """Tests another regular use case for the concat function when the previous test inputs are switched."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(ys, xs) == [4, 5, 6, 1, 2, 3]


def test_concat_edge_1() -> None:
    """Tests an edge case for the concat function when one of the lists is empty."""
    xs: list[int] = []
    ys: list[int] = [2, 0]
    assert concat(xs, ys) == [2, 0]


def test_concat_edge_2() -> None:
    """Tests an edge case for the concat function when both of the lists are empty."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []