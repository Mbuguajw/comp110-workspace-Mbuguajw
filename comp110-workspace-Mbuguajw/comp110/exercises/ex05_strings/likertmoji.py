"""Turning numbers into feelings, or in this case emojis."""
__author__ = "730329579"

cowboy: str = "\U0001F920"
grinning_face: str = "\U0001F603"
neutral_face: str = "\U0001F610"
crying_emo: str = "\U0001F62D"
upside_down_emo: str = "\U0001F643"


def represent(rating: int) -> str:
    """A function that responds accordingly to rating based on where it falls in a range of #s."""
    if rating > 5:
        return cowboy
    elif rating == 5:
        return grinning_face
    elif rating == 4:
        return grinning_face
    elif rating == 3:
        return neutral_face
    elif rating == 2:
        return crying_emo
    elif rating == 1:
        return crying_emo
    else:
        return upside_down_emo
    

def main() -> None:
    """Executes the represent function with the input."""
    numeral: str = input("How do you feel on a scale of 1-5? ")
    print(f"{represent(int(numeral))}")


if __name__ == "__main__":
    main()