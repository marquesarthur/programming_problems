import unittest
from interviewbit.math.numbers_of_length_n_and_value_less_than_k import Solution


class TestLessThan(unittest.TestCase):

    def test_base_case(self):
        s = Solution()
        A = [0, 1, 5]
        B = 1
        C = 2
        Z = 2
        result = s.nearestGT(A, B, C)
        self.assertEqual(result, Z)

    # def test_other_case(self):
    #     s = Solution()
    #     A = [5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]
    #     B = 80
    #     result = s.maxSpecialProduct(A)
    #     self.assertEqual(result, B)
