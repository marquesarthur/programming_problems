import unittest
from interviewbit.codersbit.airplane_travel_distances import Solution


class TravelTest(unittest.TestCase):


    def test_base_case(self):
        s = Solution()

        N = 20
        forward = [[1, 8], [2, 7], [3, 14]]
        backward = [[1, 5], [2, 10], [3, 14]]
        expected = [[3, 1]]
        result = s.solve(forward, backward, N)
        self.assertEqual(result, expected)

    def test_other_case(self):
        s = Solution()

        N = 20
        forward = [[1, 8], [2, 15], [3, 9]]
        backward = [[1, 8], [2, 11], [3, 12]]
        expected = [[1, 3], [3, 2]]
        result = s.solve(forward, backward, N)
        self.assertEqual(result, expected)
