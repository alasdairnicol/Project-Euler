"""
Project Euler Problem 6

http://projecteuler.net/index.php?section=problems&id=6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def solution():
    return sum(xrange(1,101))**2 - sum(x**2 for x in xrange(1,101)) 

if __name__ == "__main__":
    print solution()
