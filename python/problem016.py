"""
Project Euler Problem 16

http://projecteuler.net/index.php?section=problems&id=16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""
def solution():
    """
    Lets python do the heavy lifting
    """
    return sum(int(x) for x in str(2**1000))

if __name__ == "__main__":
    print solution()
