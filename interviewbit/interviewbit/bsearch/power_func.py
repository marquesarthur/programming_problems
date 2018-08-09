class Solution:

    def rPow(self, x, n, d):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.rPow(x, abs(n))

        if n % 2 == 0:
            result = self.rPow(x, n / 2, d)
            result = result * result
            return result % d
        else:
            return (x * self.rPow(x, n - 1, d)) % d

    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        # what if d == 0

        return self.rPow(x, n, d) % d

A = 71045970
B = 41535484
C = 64735492

x = Solution().pow(A, B, C)
print(x)
print(x == 20805472)