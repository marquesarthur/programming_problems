import unittest
from interviewbit.arrays import max_cont_sum


class TestMaxSubArray(unittest.TestCase):
    def test_base_case(self):
        s = max_cont_sum.Solution()
        A = [ 56, -451, -222, 80, -57, -85, -304, -108, 95, -377, -282, -260, -497, -471, -97, -350, -147, 62, -447, -229, 78, -165, -333, -427, -59, -338, 60, -207, -247, -431, -54, -240, -426, -123, -209, 57, -74, -287, -70, -292, 45, -278, -408, -129, -35, 65, -77, -230, -426, 20, -402, -375, -449, -280, -125, -15, -21, -327, -366, 64, -211, -414, -307 ]
        B = 95
        result = s.maxSubArray(A)
        self.assertEqual(result, B)