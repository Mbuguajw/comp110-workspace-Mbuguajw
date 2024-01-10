print("Guess a number...")
guess: int = int(input("Guess: "))
if guess == 42:
    print("Correct")
else:
    if guess > 42:
        print("Too high!")
        print("Try again.")
    else:
        print("Too low!")
        print("Try again.")
print("Game Over")


def main() -> None:
    x: int = 4
    y: int = f(x)
    print(x, y)


def f(n: int) -> int:
    x: int = n + 1
    return x


main()