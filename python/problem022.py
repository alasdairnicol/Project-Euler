"""
Project Euler Problem 21

http://projecteuler.net/index.php?section=problems&id=21

Using names.txt a 46K text file containing over five-thousand first
names, begin by sorting it into alphabetical order. Then working out
the alphabetical value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938 53 = 49714.

What is the total of all the name scores in the file?
"""
import string
scores = dict(zip(string.ascii_uppercase, xrange(1, 27)))

def name_value(word):
    """
    Calculates the sum of the values of the word's letters

    e.g. COLIN = 3 + 15 + 12 + 9 + 14 = 53
    """
    return sum(scores[l] for l in word)

def read_names():
    """
    Returns the list of names from names.txt
    """
    f = open('names.txt', 'r')
    names = f.read().replace('"', '').split(',')
    f.close()
    return names

def solution():
    """
    Lets python do the heavy lifting
    """
    names = read_names()
    names.sort()
    # Calculate alphabetical value of each name
    values = (name_value(name) for name in names)
    # Calculate score of each name (position * alphabetical value)
    scores = map(lambda x:x[0]*x[1], enumerate(values, 1))

    return sum(scores)

if __name__ == "__main__":
    print solution()
