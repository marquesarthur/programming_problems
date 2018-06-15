class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
    	if A < 0:
    		return False

    	reverseA = int(str(A)[:: -1])

    	return A - reverseA == 0

assert(Solution().isPalindrome(1) == True)
assert(Solution().isPalindrome(12) == False)
assert(Solution().isPalindrome(11) == True)
assert(Solution().isPalindrome(12121) == True)
assert(Solution().isPalindrome(111) == True)
assert(Solution().isPalindrome(121) == True)
assert(Solution().isPalindrome(1231) == False)
