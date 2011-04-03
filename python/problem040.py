"""
Project Euler Problem 40

http://projecteuler.net/index.php?section=problems&id=40

An irrational decimal fraction is created by concatenating the
positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value
of the following expression.

d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
"""

def solution():
    """
    Lets python do the heavy lifting
    """
    product = 1

    digits = (1, 10, 100, 1000, 10000, 100000, 1000000)
    n = 0
    position = 0
    for digit in digits:
        # increment n until we reach the digit we are interested in
        while digit > position:
            n+=1
            position +=len(str(n))
        # The digit we want is in str(n). If position == digit, then
        # it is the last digit of n. If position > digit, we want the
        # (position - digit)'th last digit of n.
        offset = position - digit
        d_n = int(str(n)[-1-offset])
        # update the product
        product *= d_n
    return product

if __name__ == "__main__":
    print solution()
