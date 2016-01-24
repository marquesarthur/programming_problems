class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):

    	m = len(A)
    	n = len(A[0])
    	
    	result = [[0 for x in range(m)] for y in range (n)]

    	a = 0
    	b = 0
    	# print "begin"
    	# print result
    	for i in xrange(m):
    		a = 0
    		for j in xrange(n):
    			# print A[m -1 -i][j]
    			# print "%s %s" %(a, b)
    			result[a][b] = A[m - 1 -i][j]
    			a += 1
    			# print "partial"
    			# print result
    		b += 1

    	# print "partial"
    	# print result
    	return result



assert(Solution().rotate([[1, 2], [3, 4]]) == [[3, 1], [4,2]])