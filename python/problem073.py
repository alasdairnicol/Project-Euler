"""
Project Euler Problem 73

http://projecteuler.net/index.php?section=problems&id=73

Consider the fraction, n/d, where n and d are positive integers. If 
n < d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, *3/8*, *2/5*, *3/7*, 1/2, 4/7, 3/5,
5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of
reduced proper fractions for d <= 12,000?

Note: The upper limit has been changed recently.


"""
from problem033 import calc_gcd

def solution():
    """
    For each of the numerators from 1 < n < 6000, loop through
    possible denominators.

    Lower bound (exclusive) for denominator is 2*n, 
    Upper bound (exclusive) for denominator is min(3*n, 12001)

    For each numerator, denominator pair, increase the count if the
    greatest common divider is 1 (i.e. if it is a reduced proper
    fraction.
    """
    count = 0
    for n in xrange(2, 6000):
        for d in xrange(2*n+1, min(3*n, 12001)):
            if calc_gcd(d, n) == 1:
                count += 1
    return count

if __name__ == "__main__":
    print solution()
