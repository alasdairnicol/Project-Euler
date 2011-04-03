"""
Project Euler Problem 19

http://projecteuler.net/index.php?section=problems&id=19

You are given the following information, but you may prefer to do some research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def is_leap_year(year):
    if year % 4:
        # Not divisible by 4
        return False
    if year % 100:
        # Divisible by 4, not a century
        return True
    if year % 400:
        # A century, not divisible by 400
        return False
    # Divisible by 400
    return True

def days_in_feb(year):
    if is_leap_year(year):
        return 29
    else:
        return 28

def days_in_month(year):
    return [31, days_in_feb(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Days(object):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

def solution():
    """
    FIXME
    """
    # start on Monday 1 Jan 1900
    day_of_week = Days.MONDAY
    # Move on to 1 Jan 1901
    for num_days in days_in_month(1900):
        day_of_week += num_days
        day_of_week %= 7

    # Start counting Sundays
    sunday_count = 0
    for year in xrange(1901, 2001):
        for num_days in days_in_month(year):
            # Increment the counter if it is a Sunday
            if day_of_week == Days.SUNDAY:
                sunday_count += 1

            # Move on to the next month
            day_of_week += num_days
            day_of_week %= 7
    return sunday_count

if __name__ == "__main__":
    print solution()
