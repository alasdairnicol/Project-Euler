"""
Project Euler Problem 24

http://projecteuler.net/index.php?section=problems&id=24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations, islice

def solution():
    """
    Let itertools.permutations do the hard work
    """
    # start slice at 1000000 - 1 because sequence is 0-indexed.
    perm = next(islice(permutations(xrange(10)), 1000000-1, 1000000))
    return reduce(lambda x,y: 10*x+y, perm)

if __name__ == "__main__":
    print solution()
