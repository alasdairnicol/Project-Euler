"""
Project Euler Problem 38

http://projecteuler.net/index.php?section=problems&id=38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital,
192384576. We will call 192384576 the concatenated product of 192 and
(1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2,
3, 4, and 5, giving the pandigital, 918273645, which is the
concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be
formed as the concatenated product of an integer with (1, 2, ..., n)
where n > 1?
"""

digits = [str(x) for x in xrange(1, 10)]

def solution():
    """
    First, note that the interger i < 9999 because

      abcde * 1 = qrstu
      abcde * 2 = vwxyz

      concatenated product is qrstuvwxyz is 10 digits long.

    Loop through the numbers 1 to 9999. Multiply by n=1,2,3,... until
    the concatenated product is at least 9 digits long. If it is 9
    digits long, check to see if it is pandigital. Keep track of the
    maximum pandigital number found so far.
    """
    max_seen = 0
    for i in xrange(1, 10000):
        x = i
        s = str(x)
        while len(s) < 9:
            x += i
            s += str(x)
        if len(s) == 9:
            # check if it's pandigital
            if sorted(s) == digits:
                max_seen = max(max_seen, int(s))
                if int(s) > max_seen:
                    max_seen = int(s)
    return max_seen

if __name__ == "__main__":
    print solution()
