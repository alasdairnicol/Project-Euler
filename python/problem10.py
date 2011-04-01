"""
Project Euler Problem 10

http://projecteuler.net/index.php?section=problems&id=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from problem3 import next_prime

def yield_primes_under(x):
    primes = next_prime()
    p = next(primes)
    while p < x:
        yield p
        p = next(primes)

def solution():
    return sum(yield_primes_under(2000000))


if __name__ == "__main__":
    print solution()
