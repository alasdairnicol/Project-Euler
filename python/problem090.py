"""
Project Euler Problem 90

http://projecteuler.net/index.php?section=problems&id=90

Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed from 6 and 4.

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""
from itertools import combinations

squares = ((0,1),
           (0,4),
           (0,9),
           (1,6),
           (2,5),
           (3,6),
           (4,9),
           (6,4),
           (8,1),
           )          

def extended_tuple(die):
    if 6 in die:
        if 9 not in die:
            die = die + (9,)
    elif 9 in die:
        if 6 not in die:
            die = die + (6,)
    return die

def can_make_squares(die1, die2):
    for s1, s2 in squares:
        if (s1 in die1 and s2 in die2) or (s2 in die1 and s1 in die2):
            continue
        else:
            return False
    return True

def solution():
    """
    For each possible combination of dice, increase the total if we
    can make every square.

    Because die1, die2 is considered to be the same as die2, die1, we
    return count / 2.  

    Because the dice are 6 and at least 7 digits (e.g 0,1,2,3,4,6,8)
    are required to construct all squares, we cannot make all the
    squares when die1 == die2. Therefore it is ok to divide the total
    by 2.
    """
    total = 0
    for die1 in combinations(xrange(10), 6):
        die1 = extended_tuple(die1)
        for die2 in combinations(xrange(10), 6):
            die2 = extended_tuple(die2)
            total += int(can_make_squares(die1, die2))
    return total / 2

if __name__ == "__main__":
    print solution()
