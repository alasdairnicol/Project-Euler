# -*- coding: utf-8 -*-
"""
Project Euler Problem 55

http://projecteuler.net/index.php?section=problems&id=55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers,
like 196, never produce a palindrome. A number that never forms a
palindrome through the reverse and add process is called a Lychrel
number. Due to the theoretical nature of these numbers, and for the
purpose of this problem, we shall assume that a number is Lychrel
until proven otherwise. In addition you are given that for every
number below ten-thousand, it will either (i) become a palindrome in
less than fifty iterations, or, (ii) no one, with all the computing
power that exists, has managed so far to map it to a palindrome. In
fact, 10677 is the first number to be shown to require over fifty
iterations before producing a palindrome: 4668731596684224866951378664
(53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
"""
def is_palindrome(x):
    s = str(x)
    while s:
        first, s, last = s[0], s[1:-1], s[-1]
        if first != last:
            return False
    return True

def reverse_int(x):
    """
    Reverses the integer x

    e.g. 123 -> 321
    """
    return int(reduce(lambda x,y: 10*int(x) + int(y), reversed(str(x))))

def assume_lychrel(x):
    """
    Returns True if the 'reverse and add' process has not arrived at a
    palindrome after 50 iterations.
    """
    for i in xrange(50):
        x += reverse_int(x)
        if is_palindrome(x):
            return False
    else:
        return True

def solution():
    """

    """
    count = 0
    for x in xrange(1,10000):
        count += int(assume_lychrel(x))
    return count

if __name__ == "__main__":
    print solution()
