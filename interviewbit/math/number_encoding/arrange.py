class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
    	references = {}

    	for i in xrange(len(A)):
    		A[i] = A[i] + (A[A[i]] % len(A))*len(A)

    	for i in xrange(len(A)):
    		A[i] = A[i] / len(A)

#     	print A

    		
#     	return A




# Solution().arrange([1, 0]) 
# Solution().arrange([1, 2, 3, 0])