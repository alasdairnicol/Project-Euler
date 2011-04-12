"""
Project Euler Problem 25

http://projecteuler.net/index.php?section=problems&id=25

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_(n-1) + F_(n-2), where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
The 12th term, F_12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibonacci_seq(max_val):
    """
    Generates the Fibonacci sequence.

    Terminates after the first item greater than or equal to max_val.
    """
    a, b = 1, 1
    while a < max_val:
        yield a
        a, b = b, a + b
    yield a

def solution():
    """
    Returns the length of the fibonacci sequence terminating after the
    first term to contain 1000 digits.
    """
    for i, f in enumerate(fibonacci_seq(10**999),1):
        pass
    return i

if __name__ == "__main__":
    print solution()
