"""
Project Euler Problem 35

http://projecteuler.net/index.php?section=problems&id=35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from problem003 import next_prime

def primes_under(x):
    s = set()
    primes = next_prime()
    p = next(primes)
    while p < x:
        s.add(p)
        p = next(primes)
    return s

def get_circular_numbers(x):
    """
    Returns all rotations of a number x

    e.g. 197 -> 197, 971, 719
    """
    s = str(x)
    ss = s * 2
    return [int(ss[n:n+len(s)]) for n in xrange(len(s))]


def solution():
    """
    Check each prime to see if it's circular. If it is, add it to the
    circular primes set. Finally, return the length of the set.

    This solution is currently inefficient because:

     * We check each circular prime once per rotation
       e.g we check 197, 971 and 719 to see if they are circular

     * We check prime numbers containing the digits [0,2,4,5,6,8]
       These cannot be prime because they have a rotation which is
       even or divisible by 5.

     * However I believe the prime sieve is the most inefficient part.
    """
    primes = primes_under(1000000)
    circular_primes = set()
    for p in primes:
        circular_numbers = get_circular_numbers(p)
        for c in circular_numbers[1:]: # we know that first number is prime
            if c not in primes:
                break
        else:
            circular_primes.update(set(circular_numbers))
            
    return len(circular_primes)


if __name__ == "__main__":
    print solution()
