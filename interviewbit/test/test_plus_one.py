import unittest
from interviewbit.arrays import plus_one


class TestPlusOne(unittest.TestCase):
    def test_base_case(self):
        s = plus_one.Solution()
        A = [0, 1, 1]
        B = [1, 2]
        result = s.plusOne(A)
        self.assertEqual(result, B)

    def test_nines_case(self):
        s = plus_one.Solution()
        A = [ 9, 9, 9 ]
        B = [1, 0, 0, 0]
        result = s.plusOne(A)
        self.assertEqual(result, B)
