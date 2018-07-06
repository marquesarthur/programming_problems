import unittest
from interviewbit.arrays import largest_number


class TestLargestNumber(unittest.TestCase):

    def test_base_case(self):
        s = largest_number.Solution()
        A = [3, 30, 34, 5, 9]
        B = str(9534330)
        result = s.largestNumber(A)
        self.assertEqual(result, B)


    def test_corner_case(self):
        s = largest_number.Solution()
        A = [27, 271]
        B = str(27271)
        result = s.largestNumber(A)
        self.assertEqual(result, B)

    def test_error_case(self):
        A = [472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412]
        s = largest_number.Solution()
        B = str(9648527226766636354854724412368319)
        result = s.largestNumber(A)
        self.assertEqual(result, B)

    def test_error_case_2(self):
        A = [0, 0, 0]
        s = largest_number.Solution()
        B = str(0)
        result = s.largestNumber(A)
        self.assertEqual(result, B)
