class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):

    	while B:
        	A, B = B, A%B
    	return A

assert(Solution().gcd(6, 9) == 3)
assert(Solution().gcd(9, 6) == 3)
assert(Solution().gcd(17, 13) == 1)
assert(Solution().gcd(1, 0) == 1)
assert(Solution().gcd(5, 0) == 5)
assert(Solution().gcd(0, 7) == 7)