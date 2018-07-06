class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):

        aux = {}
        for i in range(len(A)):
            if A[i] in aux:
                return A[i]
            aux[A[i]] = True

        return -1