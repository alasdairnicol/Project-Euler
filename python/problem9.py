"""
Project Euler Problem 9

http://projecteuler.net/index.php?section=problems&id=9

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_triplet(a, b, c):
    """
    Returns True if a, b, c is a Pythagorean triplet

    ie a**2 + b**2 == c**2 
    """
    return a**2 + b**2 == c**2

def solution():
    """
    Max value for a can be 332 because 332 + 333 + 335 = 1000 is the
    largest a for which a + b + c = 1000 and a < b < c.
    """
    # Check every a up to 332
    for a in xrange(1, 333):
        # Check every b > a
        for b in xrange(a+1, 1000):
            # Calculate c
            c = 1000 - a - b
            if b == c:
                # b is too large, move on to next a
                break
            if is_triplet(a,b,c):
                return a*b*c

if __name__ == "__main__":
    print solution()
