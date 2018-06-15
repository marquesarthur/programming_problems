import math

class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):

    	if A <= 1:
    		return 0

    	for i in xrange(2, int(math.sqrt(A)) + 1):
    		if A % i == 0:
    			return 0



    	return 1




assert(Solution().isPrime(6) == 0)
assert(Solution().isPrime(7) == 1)
assert(Solution().isPrime(2) == 1)
assert(Solution().isPrime(3) == 1)
assert(Solution().isPrime(4) == 0)
assert(Solution().isPrime(36) == 0)
assert(Solution().isPrime(31) == 1)
assert(Solution().isPrime(11) == 1)