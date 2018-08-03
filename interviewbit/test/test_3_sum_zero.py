import unittest
from interviewbit.pointers.three_sum_zero import Solution


class ThreeZeroSumTest(unittest.TestCase):
    
    def test_base_case(self):
        s = Solution()
        A = [-1, 0, 1, 2, -1, -4]
        A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
        B = [(-1, 0, 1), (-1, -1, 2)]

        result = s.threeSum(A)
        self.assertEqual(result, B)
