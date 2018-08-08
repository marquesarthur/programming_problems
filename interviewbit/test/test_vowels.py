import unittest
from interviewbit.codersbit.vowels import Solution


class VowelsTest(unittest.TestCase):
    
    def test_base_case(self):
        s = Solution()

        N = 1
        B = 5
        result = s.solve(N)
        self.assertEqual(result, B)

    def test_other_case(self):
        s = Solution()
        N = 2
        B = 11
        result = s.solve(N)
        self.assertEqual(result, B)

    def test_time_out(self):
        s = Solution()
        N = 80
        B = 52893034
        result = s.solve(N)
        self.assertEqual(result, B)
        #  =
