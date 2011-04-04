"""
Project Euler Problem 56

http://projecteuler.net/index.php?section=problems&id=56

A googol (10**100) is a massive number: one followed by one-hundred
zeros; 100**100 is almost unimaginably large: one followed by
two-hundred zeros. Despite their size, the sum of the digits in each
number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what
is the maximum digital sum?
"""

def sum_of_digits(x):
    return sum(int(d) for d in str(x))

def solution():
    max_digital_sum = 0
    for a in xrange(1, 100):
        for b in xrange(1, 100):
            max_digital_sum = max(max_digital_sum, sum_of_digits(a**b))
    return max_digital_sum

if __name__ == "__main__":
    print solution()
