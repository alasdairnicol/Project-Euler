# -*- coding: utf-8 -*-
"""
Project Euler Problem 33

http://projecteuler.net/index.php?section=problems&id=33

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

def calc_gcd(a,b):
    """
    Returns the greatest common divisor of a and b
    """
    a, b = max(a,b), min(a,b)
    while b:
        a, b = b, a % b
    return a

def lowest_common_terms(numerator, denominator):
    """
    Returns a tuple x, y where x/y is numerator/denominator in its
    lowest common terms.
    """
    while True:
        gcd = calc_gcd(numerator, denominator)
        if gcd == 1:
            return numerator, denominator
        numerator, denominator = (numerator/gcd), (denominator/gcd)

def is_curious(numerator, denominator):
    """
    Returns True if numerator/denominator is curious.
    """
    n1, n2 = [int(x) for x in str(numerator)]
    d1, d2 = [int(x) for x in str(denominator)]
    if (n2 == d2 == 0):
        # Ignore trivial case e.g. 30/50
        return False
    if n1 == d1:
        # does numerator/denominator = n2/d2
        if numerator*d2 == denominator * n2:
            return True
    elif n1 == d2:
        # does numerator/denominator = n2/d1
        if numerator*d1 == denominator * n2:
            return True
    elif n2 == d1:
        # does numerator/denominator = n1/d2
        if numerator*d2 == denominator * n1:
            return True
    elif n2 == d2:
        # does numerator/denominator = n1/d1
        if numerator*d1 == denominator * n1:
            return True
    return False

def solution():
    """
    Lets python do the heavy lifting
    """
    curious_fractions = []
    for numerator in xrange(10, 100):
        for denominator in xrange(numerator + 1, 100):
            if is_curious(numerator, denominator):
                curious_fractions.append((numerator, denominator))
    numerators, denominators = zip(*curious_fractions)
    # calculate numerator and denominator of product of curious fractions
    n, d = [reduce(lambda x,y:x*y, d) for d in numerators, denominators]
    n, d = lowest_common_terms(n, d)
    return d

if __name__ == "__main__":
    print solution()
