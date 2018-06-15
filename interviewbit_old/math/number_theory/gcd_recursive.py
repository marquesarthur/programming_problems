class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, a, b):
        if (b == 0):
		    return a
        else:
		    return self.gcd(b, a%b)

assert(Solution().gcd(6, 9) == 3)
assert(Solution().gcd(9, 6) == 3)
assert(Solution().gcd(17, 13) == 1)
assert(Solution().gcd(1, 0) == 1)
assert(Solution().gcd(5, 0) == 5)
assert(Solution().gcd(0, 7) == 7)