"""
Project Euler Problem 97

http://projecteuler.net/index.php?section=problems&id=97

The first known prime found to exceed one million digits was
discovered in 1999, and is a Mersenne prime of the form 2**6972593-1; it
contains exactly 2,098,960 digits. Subsequently other Mersenne primes,
of the form 2**p-1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which
contains 2,357,207 digits: 28433x27830457+1.

Find the last ten digits of this prime number.
"""

def solution():
    """
    Multiply 28433 by 2 7830457 times. At each stage, only store the last 10 digits. Finally, add 1, and return the last ten digits of the result.
    """
    num = 28433
    for x in xrange(7830457):
        num *= 2
        # We are only interested in the last 10 digits
        num %= 10**10
    num += 1
    return num % 10**10

if __name__ == "__main__":
    print solution()
