"""
Project Euler Problem 15

http://projecteuler.net/index.php?section=problems&id=15

Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
"""
from math import factorial

def n_choose_r(n, r):
    return factorial(n)/factorial(r)/factorial(n-r)

def solution():
    """
    Consider the 2x2 grid. There are 6 routes.

      rrdd
      rdrd
      rddr
      drrd
      drdr
      ddrr
    
    where r is a move right and d is a move down.

    This is 4 choose 2 ways = 4!/(2!*(4-2)!)

    So for a 20x20 grid, there are 40 choose 20 ways of arranging 40
    moves, 20 of which are down and 20 of which are right.
    """
    return n_choose_r(40, 20)

if __name__ == "__main__":
    print solution()
