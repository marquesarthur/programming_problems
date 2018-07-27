import unittest
from interviewbit.math.rearrange_array import IntegerSolution, StringSolution


class TestRearrange(unittest.TestCase):
    def test_string(self):
        A = [4, 0, 2, 1, 3]
        B = [3, 4, 2, 0, 1]

        s = StringSolution()
        result = s.arrange(A)
        self.assertEqual(result, B)

    def test_integer(self):
        A = [4, 0, 2, 1, 3]
        B = [3, 4, 2, 0, 1]

        s = IntegerSolution()
        result = s.arrange(A)
        self.assertEqual(result, B)
