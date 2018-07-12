import unittest
from interviewbit.arrays.merge_overlapping_intervals import Solution, Interval


class TestExcelColumnNumber(unittest.TestCase):

    # def test_base_case(self):
    #     s = Solution()
    #     A = [
    #         Interval(1, 10),
    #         Interval(2, 9),
    #         Interval(3, 8),
    #         Interval(4, 7),
    #         Interval(5, 6),
    #         Interval(6, 6)
    #     ]
    #     B = [Interval(1, 10)]
    #     result = s.merge(A)
    #     self.assertEqual([(x.start, x.end) for x in result], [(y.start, y.end) for y in B])

    def test_base_case(self):
        # [1,3],[2,6],[8,10],[15,18]
        s = Solution()
        A = [
            Interval(1, 3),
            Interval(2, 6),
            Interval(8, 10),
            Interval(15, 18)
        ]
        B = [Interval(1, 6), Interval(8, 10), Interval(15, 18)]
        result = s.merge(A)
        self.assertEqual([(x.start, x.end) for x in result], [(y.start, y.end) for y in B])
