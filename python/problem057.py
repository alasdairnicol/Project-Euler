"""
Project Euler Problem 57

http://projecteuler.net/index.php?section=problems&id=57

It is possible to show that the square root of two can be expressed as
an infinite continued fraction.

 sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the
eighth expansion, 1393/985, is the first example where the number of
digits in the numerator exceeds the number of digits in the
denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""
def generate_continued_fractions():
    """
    Generates a sequence of (a,b) tuples representing a/b in the
    continued fraction for sqrt(2)
    """
    a, b = 3, 2 # 1 + 1/2 = 3/2
    yield a, b
    while True:
        a, b = a+b, b  # 1 + 1/x -> 2 + 1/x (= y)
        b, a = a, b    # y -> 1/y = z
        a, b = a+b, b  # z -> 1 + z
        yield a, b

def num_digits(x):
    return len(str(x))

def is_top_heavy(a, b):
    """
    Returns True if a contains more digits than b
    """
    return num_digits(a) > num_digits(b)

def solution():
    """
    Generate the first 1000 approximations of sqrt 2. Count how many
    have more digits in the numerator than the denominator.
    """
    count = 0
    continued_fraction = generate_continued_fractions()

    for x in xrange(1000):
        a,b = next(continued_fraction)
        count += int(is_top_heavy(a,b))
    return count
                

if __name__ == "__main__":
    print solution()
