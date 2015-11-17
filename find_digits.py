# Implementation of find digits exercise
# By: Jacob Rockland

import unittest

"""
You are given an integer N. Find the digits in this number that exactly divide N
(division that leaves 0 as remainder) and display their count. For N=24, there
are 2 digits (2 & 4). Both of these digits exactly divide 24 so our answer is 2.
"""

# digits generator
def digits(num):
    while num:
        digit = num % 10
        yield digit
        num /= 10

# find digits function
def find_digits(num):
    divs = [digit for digit in digits(num) if digit != 0 and num % digit == 0]
    return len(divs)

# test methods
class TestFindDigits(unittest.TestCase):

    def test_digits(self):
        self.assertEquals(list(digits(30150)), [0, 5, 1, 0, 3])
        self.assertEquals(list(digits(135)), [5, 3, 1])
        self.assertEquals(list(digits(3)), [3])

    def find_digits(self):
        self.assertEquals(find_digits(122), 2)
        self.assertEquals(find_digits(1012), 3)
        self.assertEquals(find_digits(11), 2)
        self.assertEquals(find_digits(88), 0)
        self.assertEquals(find_digits(77), 0)

if __name__ == '__main__':
    unittest.main()
