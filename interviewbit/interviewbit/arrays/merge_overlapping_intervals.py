# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if intervals is None:
            return []

        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x: (x.end, x.start), reverse=True)

        result = []
        i = 0
        _current = intervals[i]
        while i < len(intervals):

            if i + 1 < len(intervals):
                _next = intervals[i + 1]
                if _current.end >= _next.end and _current.start <= _next.end:
                    if _current.start > _next.start:
                        _current.start = _next.start
                    i += 1
                else:
                    i += 1
                    result.append(_current)
                    _current = intervals[i]
            else:
                result.append(_current)
                i += 1

        return sorted(result, key=lambda x: (x.start, x.end))

