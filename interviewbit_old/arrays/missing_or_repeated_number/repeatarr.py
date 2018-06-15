class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
    	count = {}
    	for i in xrange(len(A)):
    		if A[i] not in count:
    			count[A[i]] = 1
    		else:
    			return A[i]

    	return -1

assert(Solution().repeatedNumber([3, 4, 1, 4, 1]) == 4)
