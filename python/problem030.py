"""
Project Euler Problem 30

http://projecteuler.net/index.php?section=problems&id=30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_of_fifth_powers(x):
    digits = [int(d) for d in str(x)]
    return sum(d**5 for d in digits)

def calc_max_value():
    """
    For a number with d digits, the max sum is d * 9**5.

    This function finds the first value in the sequence 9, 99, ... for
    which the value is greater than the sum. We then know that the
    equality cannot be true for any number greater than the sum + 1.
    """
    start = 9
    while sum_of_fifth_powers(start) > start:
        start = start * 10 + 9
    return sum_of_fifth_powers(start) + 1

def solution():
    numbers = []
    for x in xrange(2, calc_max_value()):
        if x == sum_of_fifth_powers(x):
            numbers.append(x)
    return sum(numbers)


if __name__ == "__main__":
    print solution()
