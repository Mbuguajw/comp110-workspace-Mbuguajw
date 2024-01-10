"""Some notes on using Tuples."""

from typing import Tuple

# To declare a variable, parameter or return type of Tuple
# Impot its name from the typing library and write:
# Tuple [....] where ... is the list of types
origin: Tuple[float, float] = (0.0, 0.0)

mixed_types: Tuple[int, str, bool] = (110, "is great", True)

# tuples are immutable! After construction, their items
# cannot be changed!
# ERROR EXAMPLE -- mixed_types[0] = 116

# Exercise:
# Write a function named transpose
# That takes in a Tuple[float, float] and a float offset 
# Returns a tuple that is a copy of the original where each of its 
# two components are incremented by the offset.


def transpose(point: Tuple[float, float], increment: float) -> tuple:
    new_x: float = point[0] + increment
    new_y: float = point[1] + increment
    result: Tuple[float, float] = (new_x, new_y)
    return result


test_value: Tuple[float, float] = (10.0, 20.0)
print(transpose(test_value, 10.0))