from collections import defaultdict
import sys


class Solution(object):

    def optimal(self, companies, times):

        conflicts = defaultdict(int)
        for c, t in zip(companies, times):
            if c not in conflicts:
                conflicts[c] = t
            else:
                conflicts[c] = min(conflicts[c], t)

        # computes ending time
        for arriving_time in sorted(conflicts.keys()):
            conflicts[arriving_time] = conflicts[arriving_time] + arriving_time

        max_companies, end = 0, -sys.maxint - 1
        for i in sorted(conflicts.keys()):

            if i >= end:
                max_companies += 1
                end = conflicts[i]

        return max_companies

    def universityCareerFair(self, arrival, duration):
        aux = sorted(
            list(zip(arrival, duration)),
            key=lambda p: (sum(p), p[1])
        )
        ans, end = 0, -float('inf')
        for arr, dur in aux:
            if arr >= end:
                ans, end = ans + 1, arr + dur
        return ans


A, B = [1, 3, 3, 5, 7], [2, 2, 1, 2, 1]
print(Solution().universityCareerFair(A, B))
print(Solution().optimal(A, B))

A, B = [1, 2], [7, 3]
print(Solution().universityCareerFair(A, B))
print(Solution().optimal(A, B))

A, B = [1, 3, 4, 6], [4, 3, 3, 2]
print(Solution().universityCareerFair(A, B))
print(Solution().optimal(A, B))
