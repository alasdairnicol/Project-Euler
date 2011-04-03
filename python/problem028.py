"""
Project Euler Problem 28

http://projecteuler.net/index.php?section=problems&id=28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def yield_diagonals():
    """
    Yields a sequence of lists, each containing the diagonals for
    increasing from an n x n to an (n+2) x (n+2) spiral

    output: [[1], [3,5,7,9], [13,17,21,25], ... 
    """
    # The 1x1 spiral is a special case
    a = 1
    yield [a,]

    diff = 2
    while True:
        yield [a+diff, a+2*diff, a+3*diff, a+4*diff]
        a += 4*diff
        diff += 2

def solution():
    """
    To calculate sum of diagonals on n x n spiral, we need to
    calculate (n+1)/2 terms of the sequence.
    """
    num_terms = (1001 + 1) / 2
    total = 0
    diagonals = yield_diagonals()
    for x in xrange(num_terms):
        total += sum(next(diagonals))

    return total

if __name__ == "__main__":
    print solution()
