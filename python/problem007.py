"""
Project Euler Problem 7

http://projecteuler.net/index.php?section=problems&id=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
from problem3 import next_prime

def solution():
    primes = next_prime()
    # Throw away the first 10000
    for x in xrange(10000):
        next(primes)
    # Here's the 10001st
    return next(primes)

if __name__ == "__main__":
    print solution()
