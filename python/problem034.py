"""
Project Euler Problem 34

http://projecteuler.net/index.php?section=problems&id=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial

def sum_of_factorials(x):
    digits = (int(d) for d in str(x))
    return sum(factorial(d) for d in digits)

def calc_max_value():
    """
    For a number with d digits, the max sum is d * 9!.

    This function finds the first value in the sequence 9, 99, ... for
    which the value is greater than the sum. We then know that the
    equality cannot be true for any number greater than the sum + 1.
    """
    start = 9
    while sum_of_factorials(start) > start:
        start = start * 10 + 9
    return sum_of_factorials(start) + 1

def solution():
    numbers = []
    # Single digits numbers not included. Start at 10.
    for x in xrange(10, calc_max_value()):
        if x == sum_of_factorials(x):
            numbers.append(x)
    return sum(numbers)

if __name__ == "__main__":
    print solution()
