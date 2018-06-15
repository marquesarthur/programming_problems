class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        primes = [1]*(A+1)
        primes[0] = 0
        primes[1] = 0
        sqrtN = int(A**0.5)
        for i in range(2,sqrtN+1):
            if primes[i] == 1:
                for j in range(i*i, A+1, i):
                    primes[j] = 0
        ret = []
        for i in range(2,A+1):
            if primes[i] == 1:
                ret.append(i)
        return ret


assert(Solution().sieve(7) == [2, 3, 5, 7])