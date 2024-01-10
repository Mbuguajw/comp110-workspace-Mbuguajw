"""Quiz #0 code that will be completed wholly."""
__author__ = "730329579"

import random


def roll_die(die_sides: int) -> int:
    """Question 5.1 to the quiz, creating a virtual dice."""
    return random.randint(1, die_sides)


def roll_two_dice() -> int:
    """Question 5.2 to the quiz, creating virtual die."""
    x: int = roll_die(6)
    y: int = roll_die(6)
    return x + y


def simulate(x: int, y: int) -> float:
    """Question 5.3 to the quiz, creating probabilities for different sums."""
    i: int = 0
    p: int = 0
    while i < y:
        if roll_two_dice() == x:
            p = p + 1
            i = i + 1
        else:
            i = i + 1
    chance: float = p / y
    return chance


def main() -> None:
    """Question 5.4 to the quiz, creating a list of different simulate values."""
    i: int = 1
    while i < 14:
        print(str(i) + ": " + str(simulate(i, 100000)))
        i = i + 1


main()