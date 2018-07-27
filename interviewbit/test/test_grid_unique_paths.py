import unittest
from interviewbit.math.grid_unique_paths import Solution


class TestUniquePaths(unittest.TestCase):

    def test_base_case(self):
        s = Solution()
        A = 100
        B = 1
        c = 1
        result = s.uniquePaths(A, B)
        self.assertEqual(result, c)

    # def test_other_case(self):
    #     s = Solution()
    #     A = [5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]
    #     B = 80
    #     result = s.maxSpecialProduct(A)
    #     self.assertEqual(result, B)
