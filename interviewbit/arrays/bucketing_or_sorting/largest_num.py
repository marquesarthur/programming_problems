from fractions import Fraction

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def customSort(self, a, b):
    	
    	value1 = int(a + b)
    	value2 = int(b + a)

    	return value1 - value2
    	
    		
    
    def largestNumber(self, A):
    	result = ""
    	
    	aux = map(str, A)

    	auxStr = sorted(aux, cmp=self.customSort, reverse=True)

    	for i in xrange(len(auxStr)):
    		result += auxStr[i]

    	partial = long(result)

    	return str(partial)



assert(Solution().largestNumber([3, 30, 34, 5, 9]) == "9534330")
assert(Solution().largestNumber([27, 271]) == "27271")
assert(Solution().largestNumber([12, 121 ]) == "12121")

n = 3
print(Fraction(n, 10**len(str(n))-1))
n = 30
print(Fraction(n, 10**len(str(n))-1))