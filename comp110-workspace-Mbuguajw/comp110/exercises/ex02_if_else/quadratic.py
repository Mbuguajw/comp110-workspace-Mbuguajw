"""Quadratic formula calculator code."""
__author__ = "730329579"
import math
a: str = input("Enter coefficient 'a' ")
b: str = input("Enter coefficient 'b' ")
c: str = input("Enter coefficient 'c' ")
fourac: int = (4 * int(a) * int(c))
bb: int = (int(b) ** 2)
subtract: int = (bb - fourac)
if subtract < 0:
    print("2 imaginary roots")
else:
    root: float = math.sqrt(subtract)
    sum1: float = -int(b) + root
    sum2: float = -int(b) - root
    solu1: float = sum1 / (2 * int(a))
    solu2: float = sum2 / (2 * int(a))
    if solu1 == solu2:
        print(str(solu1) + " repeated")
    else:
        print(str(solu1) + ", " + str(solu2))