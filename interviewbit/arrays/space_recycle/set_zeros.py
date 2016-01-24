class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
    	m = len(A)
    	n = len(A[0])

    	zero_rows = [0] * m
    	zero_columns = [0] * n
    	for i in xrange(m):
    		for j in xrange(n):
    			if A[i][j] == 0:
    				zero_rows[i] = 1
    				zero_columns[j] = 1

    	for i in xrange(m):
    		for j in xrange(n):
    			if zero_rows[i] == 1 or zero_columns[j] == 1:
    				A[i][j] = 0

    	return A





assert(Solution().setZeroes([[1, 0, 1], [1, 1, 1], [1, 1, 1]]) == [[0, 0, 0], [1, 0, 1], [1, 0, 1]])
assert(Solution().setZeroes([[0, 1], [1, 1]]) == [[0, 0], [0, 1]])


