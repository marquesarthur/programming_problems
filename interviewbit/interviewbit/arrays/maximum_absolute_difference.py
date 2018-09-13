# f(i, j) = |A[i] - A[j]| + |i - j| can be written in 4 ways (Since we are looking at max value, we don’t even care if the value becomes negative as long as we are also covering the max value in some way).
#
# (A[i] + i) - (A[j] + j)
# -(A[i] - i) + (A[j] - j)
# (A[i] - i) - (A[j] - j)
# (-A[i] - i) + (A[j] + j) = -(A[i] + i) + (A[j] + j)
# Note that case 1 and 4 are equivalent and so are case 2 and 3.
#
# We can construct two arrays with values: A[i] + i and A[i] - i.
# Then, for above 2 cases, we find the maximum value possible.
# For that, we just have to store minimum and maximum values of expressions A[i] + i and A[i] - i for all i.

import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        # create tuples with value and index
        # sort by increasing value and index
        # problem in the last step ?
        # do I still need all combinations? Probably no
        max1 = -(sys.maxint - 1)
        max2 = -(sys.maxint - 1)
        min1 = sys.maxint
        min2 = sys.maxint

        for i in range(len(A)):
            max1 = max(max1, A[i] + i)
            min1 = min(min1, A[i] + i)

            max2 = max(max2, A[i] - i)
            min2 = min(min2, A[i] - i)

        return max(max1 - min1, max2 - min2)


# print(Solution().maxArr([1, 3, -1]))
# print(Solution().maxArr([3, 5, 9, 1, -2, -7, 3, 4, 5, 6]))

print(Solution().maxArr([55, -8, 43, 52, 8, 59, -91, -79, -18, -94]))
