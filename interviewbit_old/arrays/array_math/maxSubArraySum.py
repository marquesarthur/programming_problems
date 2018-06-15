
# Kadanes algorithm
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        ans = 0
        mysum = 0
        hasPositive = False
        
        for i in xrange(len(A)):
            if A[i] >= 0:
                hasPositive = True
                break
            
        if hasPositive:
        
            for i in xrange(len(A)):
                if mysum + A[i] > 0:
                    mysum += A[i]
                else:
                    mysum = 0
                ans = max(ans, mysum)
        else:
            ans = A[0]
            for i in xrange(1, len(A)):
                mysum = A[i]
                ans = max(ans, mysum)

        return ans