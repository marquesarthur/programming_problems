import unittest
from interviewbit.arrays.maxspprod import Solution, CorrectSolution


class TestExcelColumnNumber(unittest.TestCase):

    def test_base_case(self):
        s = CorrectSolution()
        A = [4, 6, 5, 5, 6, 6, 5, 6, 7, 5, 5, 7, 7]
        B = 88
        result = s.maxSpecialProduct(A)
        self.assertEqual(result, B)

    # def test_other_case(self):
    #     s = Solution()
    #     A = [5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]
    #     B = 80
    #     result = s.maxSpecialProduct(A)
    #     self.assertEqual(result, B)
