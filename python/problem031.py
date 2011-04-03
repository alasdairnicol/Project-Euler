# -*- coding: utf-8 -*-
"""
Project Euler Problem 31

http://projecteuler.net/index.php?section=problems&id=31

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1 x £1 + 1 x 50p + 2 x 20p + 1 x 5p + 1 x 2p + 3 x 1p
How many different ways can £2 be made using any number of coins?
"""

COINS = (200, 100, 50, 20, 10, 5, 2, 1)

def cache(function):
    """
    Simple decorator to cache results
    """
    _cache = dict()
    def inner(*args):
        if args not in _cache:
            _cache[args] = function(*args)
        return _cache[args]
    return inner

@cache
def count_ways(amount=200, coins=COINS):
    """
    Solve recursively
    """
    count = 0
    # Consider the largest coin
    coin, coins = coins[0], coins[1:]
    # If the coin is 1p or the amount is 0, there is only one way
    if coin == 1 or not amount:
        return 1
    # For each possible number or 'coin' coins we can use, calculate
    # the number of ways of making up the remainder using smaller
    # coins. Add it to the total.
    for x in xrange(0, amount+1, coin):
        count += count_ways(amount-x, coins)
    return count

def solution():
    """
    Lets python do the heavy lifting
    """
    return count_ways(200)

if __name__ == "__main__":
    print solution()
