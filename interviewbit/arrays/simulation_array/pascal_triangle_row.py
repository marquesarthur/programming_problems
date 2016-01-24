class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):


    	if A == 0:
    		return [1]


    	previousRow = self.getRow(A - 1)
    	result = []
    	for i in xrange(len(previousRow)):
    		if i == 0:
    			result.append(1)
    		else:
    			result.append(previousRow[i] + previousRow[i -1])
    	result.append(1)

    	return result



assert(Solution().getRow(0) == [1])
assert(Solution().getRow(1) == [1, 1])
assert(Solution().getRow(2) == [1, 2, 1])
assert(Solution().getRow(3) == [1, 3, 3, 1])