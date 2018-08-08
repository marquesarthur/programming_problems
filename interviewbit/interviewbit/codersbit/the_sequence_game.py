class Solution:
    # I need a dynamic table to easy the burden of computing i^k
    ik = {}

    def compute(self, n, k):
        if k == 0:
            return 1
        if k == 1:
            return n
        elif k in self.ik:
            return self.ik[k]
        elif k % 2 == 0:
            result = self.compute(n, int(k / 2)) * self.compute(n, int(k / 2))
            self.ik[k] = result
            return result
        else:
            result = self.compute(n, 1) * self.compute(n, k - 1)
            self.ik[k] = result
            return result

    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return self.compute(A, B)

A = 17
B = 77
# A = 3
# B = 2
print(Solution().solve(A, B))
# print(Solution().solve(A, B) == 494336870)
