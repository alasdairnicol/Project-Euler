"""
Project Euler Problem 52

http://projecteuler.net/index.php?section=problems&id=52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def same_digits(x):
    """
    Returns True if x, 2x, 3x, 4x, 5x and 6x contain the same digits
    """
    digits = sorted(str(x))
    for i in xrange(2,7):
        digits2 = sorted(str(i * x))
        if digits != digits2:
            return False
    else:
        return True

def solution():
    """

    """
    x = 1
    while not same_digits(x):
        x += 1
    return x


if __name__ == "__main__":
    print solution()
