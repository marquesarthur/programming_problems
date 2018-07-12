import unittest
from interviewbit.arrays import rotate_matrix


class TestRotateMatrix(unittest.TestCase):

    def test_base_case(self):
        s = rotate_matrix.Solution()
        A = [
            [1, 2],
            [3, 4]
        ]
        B = [
            [3, 1],
            [4, 2]
        ]
        result = s.rotate(A)
        self.assertEqual(result, B)
