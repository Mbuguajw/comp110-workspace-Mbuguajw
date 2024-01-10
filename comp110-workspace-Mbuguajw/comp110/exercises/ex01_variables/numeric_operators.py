"""Mathematic madness via code."""
__author__ = "730329579"
lefthand: str = input("Left-hand side: ")
righthand: str = input("Right-hand side: ")
exponentiation: int = (int(lefthand) ** int(righthand))
division: float = (int(lefthand) / int(righthand))
integerdiv: int = (int(lefthand) // int(righthand))
remainder: int = (int(lefthand) % int(righthand))
print(lefthand + " ** " + righthand + " is " + str(exponentiation))
print(lefthand + " / " + righthand + " is " + str(division))
print(lefthand + " // " + righthand + " is " + str(integerdiv))
print(lefthand + " % " + righthand + "is" + str(remainder))