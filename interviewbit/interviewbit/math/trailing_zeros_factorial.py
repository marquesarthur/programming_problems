class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        ret = 0
        while A != 0:
            ret += (A/5)
            A /= 5
        return ret