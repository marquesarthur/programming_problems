class Solution:
    fact = {}

    def factorial(self, n):
        x = 1
        for i in range(1, n + 1):
            x *= i
        return x

    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        x = A + B - 2
        right = A - 1
        down = B - 1
        paths = self.factorial(x) / (self.factorial(right) * self.factorial(down))
        return paths
