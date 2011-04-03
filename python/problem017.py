"""
Project Euler Problem 17

http://projecteuler.net/index.php?section=problems&id=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

numbers = dict(
    (
        (1, "one"),
        (2, "two"),
        (3, "three"),
        (4, "four"),
        (5, "five"),
        (6, "six"),
        (7, "seven"),
        (8, "eight"),
        (9, "nine"),
        (10, "ten"),
        (11, "eleven"),
        (12, "twelve"),
        (13, "thirteen"),
        (14, "fourteen"),
        (15, "fifteen"),
        (16, "sixteen"),
        (17, "seventeen"),
        (18, "eighteen"),
        (19, "nineteen"),
        (20, "twenty"),
        (30, "thirty"),
        (40, "forty"),
        (50, "fifty"),
        (60, "sixty"),
        (70, "seventy"),
        (80, "eighty"),
        (90, "ninety"),
        (100, "hundred"),
        (1000, "thousand"),
        )
    )

class Number(object):
    numbers = dict(
        (
            (1, "one"),
            (2, "two"),
            (3, "three"),
            (4, "four"),
            (5, "five"),
            (6, "six"),
            (7, "seven"),
            (8, "eight"),
            (9, "nine"),
            (10, "ten"),
            (11, "eleven"),
            (12, "twelve"),
            (13, "thirteen"),
            (14, "fourteen"),
            (15, "fifteen"),
            (16, "sixteen"),
            (17, "seventeen"),
            (18, "eighteen"),
            (19, "nineteen"),
            (20, "twenty"),
            (30, "thirty"),
            (40, "forty"),
            (50, "fifty"),
            (60, "sixty"),
            (70, "seventy"),
            (80, "eighty"),
            (90, "ninety"),
            (100, "hundred"),
            (1000, "thousand"),
            )
        )
    
    def __init__(self, x, hyphens=True):
        """
        Initialises a number for the given x

        If hyphens is True, words will include hyphens by default e.g
        twenty-two
        """
        assert 1 <= x <= 9999
        self.x = x
        self.hyphens = hyphens

    def __str__(self):
        return self.as_words(hyphens=self.hyphens)

    def as_words(self, hyphens=None):
        x = self.x
        if hyphens is None:
            hyphens = self.hyphens

        thousands, hundreds, remainder = "", "", ""
        out = []
        if x / 1000:
            thousands = "%s %s" % (self.numbers[x/1000], self.numbers[1000])
            x %= 1000
            out.append(thousands)
        if x / 100:
            hundreds = "%s %s" % (self.numbers[x/100], self.numbers[100])
            x %= 100
            out.append(hundreds)
        # Add "and" if required
        if out and x:
            out.append("and")
        if x >= 20:
            # treat 11-19 separately
            tens = self.numbers[x/10*10]
            x %= 10
            if x:
                units = self.numbers[x]
                remainder = "%s-%s" % (tens, units)
            else:
                remainder = tens
            out.append(remainder)
        elif x:
            remainder = self.numbers[x]
            out.append(remainder)
        return " ".join(out)

    def num_letters(self):
        return len(str(self).replace(" ", "").replace("-", ""))

def solution():
    """
    Sums Number(x).num_letters for every number from 1 to 1000 inclusive
    """
    numbers = (Number(x) for x in xrange(1, 1001))
    return sum(x.num_letters() for x in numbers)

if __name__ == "__main__":
    print solution()
