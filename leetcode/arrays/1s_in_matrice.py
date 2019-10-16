class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])
        aux = [[0 for _ in xrange(m + 1)] for _ in xrange(n + 1)]
        maxsqlen = 0
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                prior_column = aux[i][j - 1]
                prior_line = aux[i - 1][j]
                prior_line_prior_column = aux[i - 1][j - 1]

                if matrix[i-1][j-1] == '1':
                    aux[i][j] = min(min(prior_line, prior_column), prior_line_prior_column) + 1

                maxsqlen = max(maxsqlen, aux[i][j])

        return maxsqlen**2




M = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

print(Solution().maximalSquare(M))