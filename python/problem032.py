# -*- coding: utf-8 -*-
"""
Project Euler Problem 32

http://projecteuler.net/index.php?section=problems&id=32

We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9
pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""
from itertools import permutations

def solution():
    """
    Test all permutations of  ab*cde = fghi and a*bcde=fghi.

    Store all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital in a set to prevent
    duplicates.

    Finally, return the sum of all products in the set.
    """
    products = set()

    for a,b,c,d,e,f,g,h,i in permutations(xrange(1, 10)):
        # Test ab * cde = fghi
        m1 = 10*a + b
        m2 = 100*c + 10*d +e
        product = 1000*f + 100*g + 10*h + i
        if m1 * m2 == product:
            products.add(product)
        else:
            # Test a * bcde = fghi
            m3 = a
            m4 = 1000*b + 100*c + 10*d + e
            if m3 * m4 == product:
                products.add(product)

    return sum(products)

if __name__ == "__main__":
    print solution()
