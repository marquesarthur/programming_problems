import math

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
    	# x = math.factorial(A)

    	

    	# count = 0
    	# i = 1

    	# while x % 10**i == 0:
    	# 	count += 1
    	# 	i += 1

    	# return count

    	count = 0
    	i = 5
    	while A / i >= 1:
    		count += A / i
    		i *= 5

    	return count


# assert(Solution().trailingZeroes(8775) == 2192)
# assert(Solution().trailingZeroes(4) == 0)
# assert(Solution().trailingZeroes(5) == 1)
# assert(Solution().trailingZeroes(6) == 1)
# assert(Solution().trailingZeroes(10) == 2)


