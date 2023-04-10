import unittest
from src.palindrome.KrutMorris import KrutMorris


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(KrutMorris("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(KrutMorris("hello"))

    def test_empty_string(self):
        self.assertTrue(KrutMorris(""))

    def test_single_char(self):
        self.assertTrue(KrutMorris("a"))

    def test_odd_length_palindrome(self):
        self.assertTrue(KrutMorris("level"))

    def test_even_length_palindrome(self):
        self.assertTrue(KrutMorris("deified"))


unittest.main(argv=[''], verbosity=2, exit=False)
