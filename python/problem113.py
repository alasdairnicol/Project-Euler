"""
Project Euler Problem 113

http://projecteuler.net/index.php?section=problems&id=113

Working from left-to-right if no digit is exceeded by the digit to its
left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is
called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor
decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases
such that there are only 12951 numbers below one-million that are not
bouncy and only 277032 non-bouncy numbers below 1010.

How many numbers below a googol (10100) are not bouncy?
"""
from math import factorial

def num_multicombinations(n, k):
    """
    Calculates number of muticombinations of size k from a set of
    size n.
    """
    return factorial(n+k-1)/factorial(k)/factorial(n-1)

def num_increasing(x):
    """
    Returns the number of increasing numbers with x digits

    We need to put 8 'increases' into x+1 positions.

    e.g. for 2 digit numbers: 

      ||||d|||d| = 58. four increases before first digit: 1+4 = 5
                       three increases before second digit: 5+3 = 8

    This is equivalent to the number of multicombinations of size 8
    from a set of size x + 1.
    """
    return num_multicombinations(x+1, 8)

def num_decreasing(x):
    """
    Returns the number of decreasing numbers with x digits

    Similar to num_increasing, but we now have 9 'decreases' to fit
    into x+1 positions. We need to subtract 1 because 000...0000 is
    not an x-digit number.
    """
    return num_multicombinations(x+1, 9) - 1

def num_non_bouncy(x):
    """
    Returns the number of non-bouncy numbers with x digits

    Add the number of x-digit increasing and decreasing numbers, then
    subtract 9 so that we don't count the 9 numbers which are both increasing
    and decreasing (one repeated digit e.g. 11111, 22222, ...).
     """
    return num_increasing(x) + num_decreasing(x) - 9

def solution():
    """
    Returns the sum of the number of x-digit non-bouncy numbers for
    1<=x<=100
    """
    return sum(num_non_bouncy(x) for x in xrange(1, 101))

if __name__ == "__main__":
    print solution()
