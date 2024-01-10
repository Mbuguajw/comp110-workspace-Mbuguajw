"""Find your primes!"""
__author__ = "730329579"
number: str = input("Choose a number: ")
i: int = 1
factors: int = 0
while i <= int(number):
    whole: int = int(number) % i
    if whole == 0:
        print(i)
        i = i + 1
        factors = factors + 1
    else:
        i = i + 1
if factors == 2:
    print(number + " is prime.")
else:
    print(number + " is not prime.")
