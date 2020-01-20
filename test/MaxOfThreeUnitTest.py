import unittest

from codebase.practice.MaxOfThree import MaxOfThree


class MaxOfThreeUnitTest(unittest.TestCase):

    def test_find_max_between_three_numbers_when_three_number_is_different(self):
        self.assertEqual(29, MaxOfThree().find_max(11, 5, 29))

