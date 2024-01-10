"""An example of function definitions and calls."""


def max(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b


first_number: int = int(input("First Number? "))
second_number: int = int(input("Second Number? "))
result: int = max(first_number, second_number)
third_number: int = int(input("Third Number? "))
final: int = max(result, third_number)
print(final)