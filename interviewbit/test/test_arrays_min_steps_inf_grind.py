import unittest
from interviewbit.arrays import min_steps_inf_grind


class MyTest(unittest.TestCase):
    def test_base_case(self):
        s = min_steps_inf_grind.Solution()
        A = [0, 1, 1]
        B = [0, 1, 2]
        moves = s.coverPoints(A, B)
        self.assertEqual(moves, 2)

    def test_horizontal_positive_case(self):
        s = min_steps_inf_grind.Solution()
        A = [0, 1, 2]
        B = [0, 0, 0]
        moves = s.coverPoints(A, B)
        self.assertEqual(moves, 2)

    def test_horizontal_negative_case(self):
        s = min_steps_inf_grind.Solution()
        A = [0, -1, 0]
        B = [0, 0, 0]
        moves = s.coverPoints(A, B)
        self.assertEqual(moves, 2)

    def test_vertical_positive_case(self):
        s = min_steps_inf_grind.Solution()
        A = [0, 0, 0]
        B = [0, 1, 2]
        moves = s.coverPoints(A, B)
        self.assertEqual(moves, 2)

    def test_vertical_negative_case(self):
        s = min_steps_inf_grind.Solution()
        A = [0, 0, 0]
        B = [0, -1, -2]
        moves = s.coverPoints(A, B)
        self.assertEqual(moves, 2)
