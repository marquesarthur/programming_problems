class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        bit_n = '{:b}'.format(N)
        complement = "".join(['1' if c == '0' else '0' for c in bit_n])
        return int(complement, 2)


print(Solution().bitwiseComplement(5))
print(Solution().bitwiseComplement(7))
print(Solution().bitwiseComplement(10))