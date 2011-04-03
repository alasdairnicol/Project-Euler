"""
Project Euler Problem 36

http://projecteuler.net/index.php?section=problems&id=36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
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

def is_binary_palindromic(x):
    """
    Returns True if the binary representation of x is palindromic.
    """
    s = bin(x)[2:] # bin(22)-> 0b10110, so slice off the leading '0b'.
    return is_palindromic(s)

def solution():
    """
    Only odd numbers, since an even number will end in 0 in binary.
    """
    numbers = []
    for x in xrange(1, 1000001, 2):
        if is_palindromic(x) and is_binary_palindromic(x):
            numbers.append(x)
    return sum(numbers)

if __name__ == "__main__":
    print solution()
