# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution:
    def merge(self, current_interval, new_interval):
        new_start = min(current_interval.start, new_interval.start)
        new_end = max(current_interval.end, new_interval.end)

        return Interval(new_start, new_end)

    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):

        # given X.start and X.end
        # do while i < n
        # if A[i].start < X.start and X.start <= A[i].end
        # MERGE !

        result = []

        n = len(intervals)

        i = 0
        while i < n:
            current_interval = intervals[i]

            if current_interval.start <= new_interval.start <= current_interval.end:
                new_interval = self.merge(current_interval, new_interval)
            elif new_interval.start <= current_interval.start <= new_interval.end:
                new_interval = self.merge(current_interval, new_interval)
            else:
                result.append(current_interval)

            i += 1

        result.append(new_interval)
        result = sorted(result, key=lambda k: (k.start, k.end))
        return result


A = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]

B = Interval(4, 9)

print(Solution().insert(A, B))
