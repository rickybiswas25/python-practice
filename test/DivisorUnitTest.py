import unittest
from codebase.practice.Divisor import Divisor


class DivisorUnitTest(unittest.TestCase):

    def test_do_task(self):
        expected_divisor = [1, 2, 5, 10]
        self.assertEqual(expected_divisor, Divisor().find_all_divisor(10))


