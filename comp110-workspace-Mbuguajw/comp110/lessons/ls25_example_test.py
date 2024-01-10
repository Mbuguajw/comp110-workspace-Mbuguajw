"""Demonnstration of testing!"""

from typing import List
from comp110.lessons.ls24_module import sum, fill_range


def test_fill_range_one_digit_offset() -> None:
    assert fill_range(1, 2) == [1, 2]


def test_empty_sum() -> None:
    """Example testing sum of an empty list."""
    input: List[int] = [110]
    expected_rv: int = 110
    assert sum(input) == expected_rv


def test_single_elsement_list() -> None:
    """Example testing sum of an empty list."""
    input: List[int] = [1, 2, 3]
    expected_rv: int = 6
    assert sum(input) == expected_rv
    assert sum([10, 20, 30])
