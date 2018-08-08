
# 1st example
# 2, 2, 2, 4
#
# After first iteration,
# ones = 2, twos = 0
# After second iteration,
# ones = 0, twos = 2
# After third iteration,
# ones = 0, twos = 0
# After fourth iteration,
# ones = 4, twos = 0
#


# 2nd example
# 4, 2, 2, 2
#
# After first iteration,
# ones = 4, twos = 0
# After second iteration,
# ones = 6, twos = 0
# After third iteration,
# ones = 4, twos = 2
# After fourth iteration,
# ones = 4, twos = 0

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0

        for i in range(len(A)):
            twos = twos | (ones & A[i])
            ones = ones ^ A[i]
            common_bit_mask = ~(ones & twos)
            ones &= common_bit_mask
            twos &= common_bit_mask

        return ones




Solution().singleNumber([4, 4, 4, 2])
Solution().singleNumber([4, 4, 2, 4])
Solution().singleNumber([2, 4, 4, 4])