# When i = I + 1, our A[i] increases ( as the array is sorted ).
# So, for j = J - 1, the differece will be smaller than D1
# (which is even more smaller to diff.)
# Which means we do not need to explore j <= J - 1
# and we can begin exploring directly from j = J.
# So, j only keeps moving in forward direction and never needs to come back as i increases.
#
# Let us use that in a solution now:


class OptimalSolution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i = 0
        j = 1
        while j < len(A):
            if A[j] - A[i] == B and i != j:
                return 1
            elif A[j] - A[i] > B:
                i += 1
            else:
                j += 1
        return 0

class Solution:

    def bin_search(self, A, target, start, end):
        while start <= end:
            mid = int((start + end) / 2)

            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):

        if not A:
            return 0

        for i, x in enumerate(A):
            y = B + x

            if y > x:  # search to the right
                idx = self.bin_search(A, y, i + 1, len(A) - 1)
            else:  # search to the left
                idx = self.bin_search(A, y, 0, i - 1)

            if idx != -1:
                return 1

        return 0

A = [ 2, 14, 18, 23, 25, 36, 40, 44, 44, 53, 54, 68, 71, 80, 94 ]
B = 82

print(Solution().diffPossible(A, B))