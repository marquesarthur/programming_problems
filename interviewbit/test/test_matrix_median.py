import unittest
from interviewbit.bsearch.matrix_median import Solution


class MatrixFindMedianTest(unittest.TestCase):


    def test_base_case(self):
        s = Solution()
        A = [
            [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]
        ]
        B = 5

        result = s.findMedian(A)
        self.assertEqual(result, B)

    def test_single_column_case(self):
        s = Solution()
        A = [[1], [3], [3]]
        B = 3

        result = s.findMedian(A)
        self.assertEqual(result, B)

    def test_single_column_case_2(self):
        s = Solution()
        A = [[5], [4], [3], [1], [3], [1], [4], [2], [5], [3], [3]]
        B = 3

        result = s.findMedian(A)
        self.assertEqual(result, B)
