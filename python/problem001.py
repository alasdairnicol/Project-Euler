"""
Project Euler Problem 1

http://projecteuler.net/index.php?section=problems&id=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
def sum_divisible_by(n, max_val=999):
    """
    Returns the sum of all numbers less than or equal to max_val that
    are divisible by n.
    """
    return n * (max_val/n) * (max_val/n + 1) / 2

def solution():
    """
    Add the sum of all numbers less than 1000 that are divisible by 3
    to the sum of all numbers less 1000 that are divisible by
    5. Subtract the sum of all numbers less than 1000 that are
    divisible by 15 so that we do not count those numbers twice.
    """
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)

if __name__ == "__main__":
    print solution()
