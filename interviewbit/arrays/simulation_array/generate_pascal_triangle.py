class Solution:

    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        triangle = []
        i = 0
        while i < A:
            triangle.append(self.getRow(i))
            i += 1

        #print triangle
        return triangle

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



assert(Solution().generate(1) == [[1]])
assert(Solution().generate(2) == [[1], [1, 1]])
assert(Solution().generate(3) == [[1], [1, 1], [1, 2, 1]])
assert(Solution().generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
assert(Solution().generate(5) == [[1 ], [1, 1 ], [1, 2, 1 ], [1, 3, 3, 1 ], [1, 4, 6, 4, 1 ]])