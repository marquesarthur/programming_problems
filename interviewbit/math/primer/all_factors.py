

class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        if A == 1:
            return [A]
        ret = [1,A]
        sqrtN = int(A**0.5)
        for i in range(2,sqrtN):
            if A%i == 0:
                ret.append(i)
                ret.append(A/i)

        if A%sqrtN == 0:
            ret.append(sqrtN)
            if sqrtN**2 != A:
                ret.append(A/sqrtN)
        ret.sort()
        return ret



assert(Solution().allFactors(6) == [1, 2, 3, 6])
assert(Solution().allFactors(85463) == [1, 7, 29, 203, 421, 2947, 12209, 85463])
