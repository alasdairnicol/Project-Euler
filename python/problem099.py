"""
Project Euler Problem 99

http://projecteuler.net/index.php?section=problems&id=99

Comparing two numbers written in index form like 2**11 and 3**7 is not
difficult, as any calculator would confirm that 

2**11 = 2048 < 3**7 = 2187.

However, confirming that 632382 ** 518061 > 519432 ** 525806 would be
much more difficult, as both numbers contain over three million
digits.

Using base_exp.txt, a 22K text file containing one thousand lines with
a base/exponent pair on each line, determine which line number has the
greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the
example given above.
"""
from math import log
def solution():
    """
    Calculating base ** exp is expensive, so we compare the logs
    instead, using the formula:
    
      exp * log(base) = log(base ** exp)

    We loop through the list, comparing each calculated value to the
    previous max. When we find a new maximum, we store the current row
    number. Finally, we return the row where the maximum value was
    found.
    """
    max_seen = 0
    line_where_max_seen = 0

    f = open("base_exp.txt", 'r')

    for i, line in enumerate(f.readlines(), 1):
        base, exp = [int(x) for x in line.split(",")]
        log_val = exp * log(base)
        if log_val > max_seen:
            max_seen = log_val
            line_where_max_seen = i

    return line_where_max_seen

if __name__ == "__main__":
    print solution()
