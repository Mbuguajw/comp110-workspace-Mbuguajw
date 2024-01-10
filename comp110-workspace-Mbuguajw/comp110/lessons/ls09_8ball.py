"""A magic 8 ball game."""

import random

is_playing: bool = True

while is_playing:
    question: str = input("Ask a yes/no question: ")
    response: int = random.randint(0, 2)
    if response == 0:
        print("Very doubtful")
    else:
        if response == 1:
            print("Ask again later")
        else:
            print("It is certain")
    is_playing = input("Continue? ") == "yes"
     
print("Have a nice day.")