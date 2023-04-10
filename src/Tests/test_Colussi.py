import unittest
from src.palindrome.Colussi import colussi


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(colussi("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(colussi("hello"))

    def test_empty_string(self):
        self.assertTrue(colussi(""))


unittest.main(argv=[''], verbosity=2, exit=False)