class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        primes = self.primesLessThan(A)
        # print primes
 
        for x in xrange(len(primes)):
            currentPrime = primes[x]
            complement = A - currentPrime
 
            if complement in primes:
                # print [currentPrime, complement]
                return [currentPrime, complement]
 
        return []
 
    def primesLessThan(self, A):
        primes = [1] * (A + 1)
        primes[0] = 0
        primes[1] = 0
        sqrtN = int(A**0.5)
        for i in xrange(sqrtN + 1):
            if primes[i] == 1:
                for j in xrange(i*i, A+1, i):
                    primes[j] = 0
        result = []
        for k in xrange(2, A+1):
            if primes[k] == 1:
                result.append(k)
 
        result.sort()
 
        return result
        
#assert(Solution().primesum(4) == [2, 2])
#assert(Solution().primesum(6) == [3, 3])
#assert(Solution().primesum(8) == [3, 5])