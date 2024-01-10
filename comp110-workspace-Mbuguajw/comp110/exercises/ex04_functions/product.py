"""Submission for Exercise 4."""
__author__ = "730329579"


def product(x: int, y: int) -> int:
    """Finds the products of numbers inbetween and inclusive of the ones provided."""
    i: int = 1
    if x < y:
        i = x + i
        p: int = x * i
        while i < y:
            i = 1 + i
            p = p * i 
        return p            
    else:
        if x > y:
            i = y + i
            t: int = y * i
            while i < x:
                i = 1 + i
                t = t * i 
            return t
        else:
            return y         
    

print(str(product(2, 4)))