"""
Project Euler Problem 3

http://projecteuler.net/index.php?section=problems&id=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def next_prime():
    yield 2 # The only even prime
    candidate = 3
    primes = [2,]
    while True:
        sqrt_candidate = math.sqrt(candidate)
        for p in primes:
            if p > sqrt_candidate:
                yield candidate
                primes.append(candidate)
                break
            if not candidate % p:
                # candidate is not prime
                break
        # increase the candidate by 2
        # (only test odd primes)
        candidate += 2

def solution():
    x = 600851475143
    sqrt_x = math.sqrt(x)
    factors = []
    primes = next_prime()
    p = next(primes)
    while x > 1:
        while not (x % p):
            factors.append(p)
            x /= p
        p = next(primes)

    return factors [-1]
        
if __name__ == "__main__":
    print solution()
