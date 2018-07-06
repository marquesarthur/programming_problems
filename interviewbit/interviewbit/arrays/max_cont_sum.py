from operator import itemgetter

class Solution:
    # @param A : tuple of integers
    # @return an integer
   def maxSubArray(self, A):
        best = min(A)
        sumsofar = 0
        for x in A:
            sumsofar += x
            best = max(sumsofar, best)
            # Doing this last, to handle case
            # when all numbers are negative.
            sumsofar = max(sumsofar, 0)
        return best
