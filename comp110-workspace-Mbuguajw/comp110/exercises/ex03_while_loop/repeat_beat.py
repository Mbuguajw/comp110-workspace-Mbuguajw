"""Clap to that funky beat."""
__author__ = "730329579"
sound: str = input("What beat do you want to repeat? ")
repeat: str = input("How many times do you want to repeat it? ")
i: int = 1
string: str = sound
if int(repeat) > 0:
    while i != int(repeat):
        i = i + 1
        string = string + " " + sound
    print(string)
else:
    print("No beat...")