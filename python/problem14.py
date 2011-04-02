"""
Project Euler Problem 14

http://projecteuler.net/index.php?section=problems&id=14

The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

class Chain(object):
    def __init__(self):
        self.cache = {1: 1}
        self.longest_chain_length = 1
        self.start_number_with_longest_chain = 1

    @staticmethod
    def next_item(n):
        """
        Calculates the next item in the sequence for a given n.
        """
        if n%2:
            return 3 * n + 1
        else:
            return n / 2

    def calculate_length(self, start_number):
        """
        Calculates the length of the chain starting with x.
        """
        x = start_number
        not_cached = []
        while x not in self.cache:
            # calculate the next number in the sequence
            not_cached.append(x)
            x = self.next_item(x)
        # we have now merged into an existing chain!
        not_cached.reverse()
        for length, val in enumerate(not_cached, 1 + self.cache[x]):
            self.cache[val] = length
        return length

    def update_longest_chain(self, start_number, length):
        """
        Updates the longest_chain_length and start_number_with_longest_chain
        attributes if we have found a new longest chain.
        """
        if length > self.longest_chain_length:
            self.start_number_with_longest_chain = start_number
            self.longest_chain_length = length

def solution():
    """
    Calculate the chain lengths for all start numbers less than one
    million, and return the start number with the longest chain length.
    """
    c = Chain()
    for x in xrange(2,1000000):
        if x not in c.cache:
            length = c.calculate_length(x)
            c.update_longest_chain(x, length)
    return c.start_number_with_longest_chain

if __name__ == "__main__":
    print solution()
