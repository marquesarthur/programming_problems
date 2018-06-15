from string import Formatter

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
    	base = 26
    	result = 0
    	i = len(A) - 1
    	for char in A.lower():
    		current = ord(char) - 96 
    		if i > 0:
    			result += (base**i) * current
    		else:
    			result += current

    		i -= 1

    	#print "%s -> %s" %(A, result)
    	return result


assert(Solution().titleToNumber('A') == 1)
assert(Solution().titleToNumber('B') == 2)
assert(Solution().titleToNumber('C') == 3)
assert(Solution().titleToNumber('Z') == 26)
assert(Solution().titleToNumber('AA') == 27)
assert(Solution().titleToNumber('AB') == 28)
assert(Solution().titleToNumber('AAA') == 703)
assert(Solution().titleToNumber('ABC') == 731)
assert(Solution().titleToNumber('BCBA') == 37233)
