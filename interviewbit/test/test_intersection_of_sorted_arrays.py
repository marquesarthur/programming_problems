import unittest
from interviewbit.pointers.intersection_of_sorted_arrays import Solution


class TestIntersection(unittest.TestCase):
    def test_string(self):
        A = [4, 0, 2, 1, 3]
        B = [3, 4, 2, 0, 1]

        s = Solution()
        C = [35, 38, 53, 67, 69, 94, 98]
        result = s.intersect(A, B)
        self.assertEqual(result, B)
