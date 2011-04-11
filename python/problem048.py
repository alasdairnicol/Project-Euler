"""
Project Euler Problem 48

http://projecteuler.net/index.php?section=problems&id=48

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series:

  1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

def solution():
    """
    For each x from 1 to 1000, calculate (x ** x) % 10**10, and add to
    the total. 

    Return total % 10**10.
    """
    total = 0
    for i in xrange(1, 1000):
        x = i
        for j in xrange(1, i):
            x *= i
            x %= 10 ** 10
        total += x
    return total % 10**10

if __name__ == "__main__":
    print solution()
