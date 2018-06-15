import math

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        return math.factorial(A+B-2)/(math.factorial(A-1)*math.factorial(B-1))

        

# assert(Solution().uniquePaths(1, 3000) == 1)
# assert(Solution().uniquePaths(3000, 1) == 1)
# assert(Solution().uniquePaths(2, 2) == 2)
# assert(Solution().uniquePaths(3, 7) == 28)
# assert(Solution().uniquePaths(15, 12) == 4457400)       




