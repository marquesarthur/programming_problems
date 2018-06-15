from fractions import Fraction
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = sorted(A, key=lambda n: Fraction(n, 10**len(str(n))-1), reverse=True)
        i = 0
        while i < len(A)-1:
            if A[i] != 0:
                break
            else:
                i+=1
        ret = map(lambda x:str(x),A[i:])
        return ''.join(ret)
