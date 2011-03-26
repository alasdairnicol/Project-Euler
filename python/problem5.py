"""
Project Euler Problem 5

http://projecteuler.net/index.php?section=problems&id=5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""
from collections import defaultdict

# FIXME generate these programmatically
prime_factorisations = {
    1: {},
    2: {2: 1,},
    3: {3: 1,},
    4: {2: 2,},
    5: {5: 1,},
    6: {2: 1, 3: 1},
    7: {7: 1,},
    8: {2: 3,},
    9: {3: 2,},
    10: {2: 1, 5: 1},
    11: {11: 1,},
    12: {2: 2, 3: 1},
    13: {13: 1,},
    14: {2: 1, 7: 1},
    15: {3: 1, 5: 1},
    16: {2: 4,},
    17: {17: 1,},
    18: {2: 1, 3: 2},
    19: {19: 1,},
    20: {2: 2, 5:1},
    }

def solution():
    factors = defaultdict(int)
    for d in prime_factorisations.values():
        for prime, num in d.items():
            factors[prime] = max(factors[prime], num)

    # Calculate the product of all the factors
    return reduce(lambda x,y:x*y, [f**num for f, num in factors.items()])


if __name__ == "__main__":
    print solution()
