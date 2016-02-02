

class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        binary = ''
        base = 2

        if A == 0:
            binary = str(0)
        elif A == 1:
            binary = str(1)
        
        mod = A % base
        while A / base > 0:
            mod = A % base
            
            A = A / base
            binary = str(mod) + binary
            if A == 1:
                binary = str(A) + binary
                break
            
                

        return binary

assert(Solution().findDigitsInBinary(0) == '0')
assert(Solution().findDigitsInBinary(1) == '1')
assert(Solution().findDigitsInBinary(2) == '10')
assert(Solution().findDigitsInBinary(5) == '101')
assert(Solution().findDigitsInBinary(3) == '11')
assert(Solution().findDigitsInBinary(15) == '1111')
