class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):

    	result = []
    	A.sort()

    	i = 0
    	while i < len(A):
    		if i + 1 < len(A):
    			A[i], A[i + 1] = A[i+1], A[i]

    		i += 2

    	for i in xrange(len(A)):
    		result.append(A[i])

    	return result

   




assert(Solution().wave([1]) == [1])
assert(Solution().wave([1, 2]) == [2, 1])
assert(Solution().wave([1, 2, 3, 4]) == [2, 1, 4, 3])