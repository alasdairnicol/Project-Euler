"""
Project Euler Problem 1

http://projecteuler.net/index.php?section=problems&id=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def solution():
    """
    Loops through all numbers from 1 to 999.

    Adds number to total if x is divisible by 3 or 5
    """
    total = 0
    for x in xrange(1000):
        if not x % 3 or not x % 5:
            total += x

    return total

if __name__ == "__main__":
    print solution()
