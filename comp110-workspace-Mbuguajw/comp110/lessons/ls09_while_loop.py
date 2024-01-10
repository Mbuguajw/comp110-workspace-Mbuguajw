"""A while loop demo."""

iterations: int = int(input("Loop how many times? "))
i: int = 0
while i < iterations:
    print("In repeat block!")
    print("I love you! " + str(i))
    i = i + 1

print("After repeat block")
print("i's terminal value is " + str(i))