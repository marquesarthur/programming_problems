import unittest
from interviewbit.pointers.min_absolute_diff import Solution


class MinAbsoluteDiffTest(unittest.TestCase):


    def test_base_case(self):
        s = Solution()

        expected = 1
        A = [1, 4, 5, 8, 10]
        B = [6, 9, 15]
        C = [2, 3, 6, 6]
        result = s.solve(A, B, C)
        self.assertEqual(result, expected)

    def test_other_case(self):
        s = Solution()

        expected = 5
        A = [1, 4, 4, 5, 6, 6]
        B = [1, 2, 3, 4]
        C = [9, 10]
        result = s.solve(A, B, C)
        self.assertEqual(result, expected)
