"""Free biscuits from the UNC Bball gameboolean."""
__author__ = "730329579"
score: str = input("How many points did UNC score? ")
print("UNC scored " + score + " points!!")
numeric_score: int = int(score)
if numeric_score >= 100:
    print("biscuits!!")
else:
    print("no biscuits.")