class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i+1,n):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for i in range(n/2):
            for j in range(n):
                tmp = A[j][n-i-1]
                A[j][n-i-1], A[j][i] = A[j][i], A[j][n-i-1]
        return A