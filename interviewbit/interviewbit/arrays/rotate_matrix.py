class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        m = len(A)
        n = len(A[0])
        result = [[0 for x in range(m)] for y in range(n)]

        a = 0
        b = 0
        for i in xrange(m):
            a = 0
            for j in xrange(n):
                result[a][b] = A[m - 1 - i][j]
                a += 1
            b += 1

        return result