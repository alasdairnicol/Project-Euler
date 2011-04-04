"""
Project Euler Problem 42

http://projecteuler.net/index.php?section=problems&id=42

The nth term of the sequence of triangle numbers is given by, 
tn = 1/2*n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word
value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a
triangle word.

Using words.txt, a 16K text
file containing nearly two-thousand common English words, how many are
triangle words?


"""
import string

def get_words():
    f = open('words.txt', 'r')
    words = f.read().replace('"',"").replace("'", "").split(",")
    return words

def triangular_number(n):
    """
    Returns's the n'th triangular number
    """
    return n*(n+1) / 2

def get_triangle_numbers(max_score):
    """
    Returns a list of all triangular numbers <= max_score
    """
    l=[]
    n = 1
    t_n = triangular_number(n)
    while t_n <= max_score:
        l.append(t_n)
        n += 1
        t_n = triangular_number(n)
    return l

letterscore = dict(zip(string.ascii_uppercase, xrange(1, 27)))

def wordscore(word):
    """
    Returns the score for a word
    """
    return sum(letterscore[l] for l in word)

def solution():
    """
    Lets python do the heavy lifting
    """
    words = get_words()
    
    # Calculate the maximum score if all letters were 'Z'
    max_length = max(len(w) for w in words)
    max_score = max_length * letterscore['Z']

    triangular_numbers = get_triangle_numbers(max_score=max_score)

    count = 0
    for word in words:
        if wordscore(word) in triangular_numbers:
            count += 1

    return count

if __name__ == "__main__":
    print solution()
