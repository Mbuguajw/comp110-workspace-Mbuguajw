"""Some factorial magic is afoot."""
__author__ = "730329579"
number: int = int(input("Choose a number: "))
i: int = 1
p: int = 1
if number == 0:
    print("Factorial: 1")
else:
    while i < number:
        i = i + 1
        p = p * i
    print("Factorial: " + str(p))