MAX_32_BIT_INT = 2147483647
MIN_32_BIT_INT = -2147483648

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
    	if A < MIN_32_BIT_INT or A > MAX_32_BIT_INT:
    		return 0

    	isNegative = False

    	if A < 0:
    		A = abs(A)
    		isNegative = True

    	reverse = int(str(A)[:: -1])
    	if isNegative:
    		reverse *= -1

    	if reverse < MIN_32_BIT_INT or reverse > MAX_32_BIT_INT:
    		return 0

    	return reverse




