"""A demo of strings as sequences of characters."""


def main() -> None:
    user_input: str = input("Give me a string... ")
    i: int = 0
    while i < len(user_input):
        print(ord(user_input[i]))
        print(chr(65 + i))
        i = i + 1

    # TODO: Write a loop starting form a counter variable of 0
    # Iterate through each character in user_input, printing out
    # each character on its own line.
    

main()