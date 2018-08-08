class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        if A == 0:
            return 0
        else:
            mod = int(A % 2)
            return mod + self.numSetBits(int(A / 2))
