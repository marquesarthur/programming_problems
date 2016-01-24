class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
    	result = []

    	print ""

    	carriage = True
    	current = 0

    	A = list(reversed(A))


    	for i in xrange(0, len(A)):
    		a = A[i]
    		

    		current = i
    		
    		if carriage:
    			carriage = (a + 1) % 10 == 0
    			newValue = (a + 1) % 10
    			result.append(newValue)
    		else:
    			break


    	if carriage:
    		result.append(1)
    	
    	print result
    	print current

    	if current >= 0 and len(A) > 1:
    		print A[0:current + 1]
    		result = A[0:current + 1] + result



    	

    	print result

    	while result[0] == 0:
    		result = result[1:]
		#print result


    	return result

assert(Solution().plusOne([1, 2, 3]) == [1, 2, 4])
assert(Solution().plusOne([]) == [1])
assert(Solution().plusOne([1]) == [2])
assert(Solution().plusOne([9]) == [1, 0])
assert(Solution().plusOne([9, 9]) == [1, 0, 0])
assert(Solution().plusOne([1, 3, 9, 9]) == [1, 4, 0, 0])
assert(Solution().plusOne([1, 1, 1, 3, 2, 1, 1, 2, 5, 9, 6, 5]) == [1, 1, 1, 3, 2, 1, 1, 2, 5, 9, 6, 6])
assert(Solution().plusOne([ 0, 3, 7, 6, 4, 0, 5, 5, 5 ]) == [3, 7, 6, 4, 0, 5, 5, 6 ])
