# -*- coding: utf-8 -*-
"""
Project Euler Problem 92

http://projecteuler.net/index.php?section=problems&id=92

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
"""

def next(x):
    return sum(int(d)**2 for d in str(x))

def solution():
    """
    This is rather slow. Loop from 1 to 9999999. Store all the numbers
    for which we have calculated the end of the sequence in the cache.

    Finally, return the size of the set of numbers where the sequence
    ends in 89.
    """
    cache = {1: set([1]),
             89: set([89]),
             }

    for i in xrange(1, 10000000):
        x = i
        chain = set([x])
        while True:
            if x in cache[1]:
                cache[1].update(chain)
                break
            elif x in cache[89]:
                cache[89].update(chain)
                break
            else:
                x = next(x)
                chain.add(x)

    return len(cache[89])

if __name__ == "__main__":
    print solution()
