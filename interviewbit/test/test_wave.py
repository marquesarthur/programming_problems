import unittest
from interviewbit.arrays import wave


class TestPlusOne(unittest.TestCase):

    def test_base_case(self):
        s = wave.Solution()
        A = [1, 2, 3, 4]
        B = [2, 1, 4, 3]
        result = s.wave(A)
        self.assertEqual(result, B)

    def test_odd_case(self):
        s = wave.Solution()
        A = [1, 3, 4]
        B = [3, 1, 4]
        result = s.wave(A)
        self.assertEqual(result, B)

