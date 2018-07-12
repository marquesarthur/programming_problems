import unittest
from interviewbit.math import excel_column_number





class TestExcelColumnNumber(unittest.TestCase):
    def test_base_case(self):
        s = excel_column_number.Solution()
        A = 'A'
        B = 1
        result = s.titleToNumber(A)
        self.assertEqual(result, B)

        A = 'B'
        B = 2
        result = s.titleToNumber(A)
        self.assertEqual(result, B)

        A = 'C'
        B = 3
        result = s.titleToNumber(A)
        self.assertEqual(result, B)

        A = 'Z'
        B = 26
        result = s.titleToNumber(A)
        self.assertEqual(result, B)

        A = 'AA'
        B = 27
        result = s.titleToNumber(A)
        self.assertEqual(result, B)

        A = 'AB'
        B = 28
        result = s.titleToNumber(A)
        self.assertEqual(result, B)

        A = 'CB'
        B = 80
        result = s.titleToNumber(A)
        self.assertEqual(result, B)

        A = 'AAC'
        B = 705
        result = s.titleToNumber(A)
        self.assertEqual(result, B)
