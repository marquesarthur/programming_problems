import unittest
from interviewbit.math import palindrome_integer


class TestPlusOne(unittest.TestCase):
    def test_base_case(self):
        s = palindrome_integer.Solution()
        A = 121
        B = True
        result = s.isPalindrome(A)
        self.assertEqual(result, B)

    def test_nines_case(self):
        s = palindrome_integer.Solution()
        A = 123
        B = False
        result = s.isPalindrome(A)
        self.assertEqual(result, B)
