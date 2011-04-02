"""
Project Euler Problem 4

http://projecteuler.net/index.php?section=problems&id=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindromic(x):
    """
    Returns True if x is a palindromic, else False
    """
    s = str(x)
    while s:
        if s[0] != s[-1]:
            return False
        s = s[1:-1] # chop off the first and last numbers
    return True

def solution():
    largest = 0
    for x in xrange(100, 1000):
        for y in xrange(x, 1000):
            if is_palindromic(x * y):
                largest = max(x*y, largest)
    return largest


if __name__ == "__main__":
    print solution()
