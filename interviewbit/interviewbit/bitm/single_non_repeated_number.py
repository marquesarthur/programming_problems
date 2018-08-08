class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        result = A[0]
        for i in range(1, len(A)):
            result ^= A[i]

        return result
