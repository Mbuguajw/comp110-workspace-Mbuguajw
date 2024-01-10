"""An abbreviation excercise for good practice."""
__author__ = "730329579"


def abbreviate(phrase: str) -> str:
    """Determines which characters in a phrase are uppercase and returns them."""
    i: int = 0
    string: str = ""
    while i < len(phrase):
        if ord(phrase[i]) < 91 and ord(phrase[i]) > 64:
            string = string + str(phrase[i])
            i = i + 1
        else:
            i = i + 1
    return string


def main() -> None:
    """Executes the abbreviate function with the input of a phrase."""
    answer: str = input("Write some text with some uppercase letters: ")
    print(f"The abbreviation is \"{abbreviate(answer)}\".")


if __name__ == "__main__":
    main()