"""Example of a Python module."""

from typing import List


def sum(input: List[int]) -> int:
    result: int = 0
    i: int = 0 
    while i < len(input):
        result += input[i]
        i += 1
    return result


def fill_range(low: int, high: int) -> List[int]:
    """Fill range by appending to a list from low to high, inclusive."""
    result: List[int] =[]
    return[]


if __name__ == "__main__"
    print(f"ls24_module loaded with {__name__}")

