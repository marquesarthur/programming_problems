import unittest
from interviewbit.arrays import find_duplicate


class TestPlusOne(unittest.TestCase):

    def test_one_duplicate(self):
        s = find_duplicate.Solution()
        A = [1, 2, 3, 2]
        B = 2
        result = s.repeatedNumber(A)
        self.assertEqual(result, B)

    def test_two_duplicates(self):
        s = find_duplicate.Solution()
        A = [1, 2, 3, 2, 3]
        B = 2
        result = s.repeatedNumber(A)
        self.assertEqual(result, B)

    def test_non_duplicate(self):
        s = find_duplicate.Solution()
        A = [1, 2, 3, 4, 5]
        B = -1
        result = s.repeatedNumber(A)
        self.assertEqual(result, B)

