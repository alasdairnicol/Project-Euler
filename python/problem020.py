"""
Project Euler Problem 20

http://projecteuler.net/index.php?section=problems&id=20

n! means n x (n-1) x  ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""
from math import factorial

def solution():
    """
    Lets python do the heavy lifting
    """
    return sum(int(x) for x in str(factorial(100)))

if __name__ == "__main__":
    print solution()
