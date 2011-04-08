"""
Project Euler Problem 112

http://projecteuler.net/index.php?section=problems&id=112

Working from left-to-right if no digit is exceeded by the digit to its
left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is
called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor
decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just
over half of the numbers below one-thousand (525) are bouncy. In fact,
the least number for which the proportion of bouncy numbers first
reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the
time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is
exactly 99%.
"""

def _is_increasing(x_as_list):
    """
    Returns True if no digit is exceeded by the digit to its left
    """
    return sorted(x_as_list) == x_as_list

def _is_decreasing(x_as_list):
    """
    Returns True if no digit is exceeded by the digit to its right
    """
    return sorted(x_as_list, reverse=True) == x_as_list

def is_bouncy(x):
    """
    Returns True if x is bouncy i.e is neither increasing or decreasing.
    """
    x_as_list = list(str(x))
    return not (_is_increasing(x_as_list) or _is_decreasing(x_as_list))

def solution():
    """
    """
    x = 1     # counter
    count = 0 # number of bouncy numbers seen

    while count * 100 / x != 99:
        count += bool(is_bouncy(x))
        x += 1

    return x

if __name__ == "__main__":
    print solution()
