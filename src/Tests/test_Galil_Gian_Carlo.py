import unittest
from src.palindrome.GalilGiancarlo import Giacarlo


class TestPalindrome(unittest.TestCase):
    # Test case 1: Palindrome with special characters
    def test_Palidrome(self):
        assert Giacarlo("A man, a plan, a canal: Panama.") == True

    # Test case 2: Non-palindrome with repeated letters
    def test_non_Palidrome(self):
        assert Giacarlo("mississippi") == False

    # Test case 3: Non-palindrome with mixed case and spaces
    def test_non_Palindrome_Mixed(self):
        assert Giacarlo("not a palindrome") == False
