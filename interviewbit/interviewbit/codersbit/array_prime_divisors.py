import math


class Solution:
    primes = [2, 3, 5, 7, 11]

    def isPrime(self, num):
        if num == 1:
            return False

        if num in self.primes:
            return True

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

        self.primes.append(num)
        return True

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        for num in A:
            if B % num == 0 and self.isPrime(num):
                count += 1
                print(num)

        return count


A = [ 272, 73, 16, 262, 440, 610, 710, 886, 973, 38, 637, 141, 904, 48, 52, 361, 257, 176, 371, 911, 999, 430, 738, 552, 250, 570, 754, 66, 832, 174, 504, 978, 646, 352, 680, 457, 975, 402, 216, 997, 1, 899, 900, 150, 844, 313 ]
B = 542

# print(Solution().solve(A, B))

A = [ 285, 57, 323, 748, 534, 32, 91, 11, 4, 615, 143, 394, 388, 958, 260, 558, 415, 84, 560, 229, 905, 37 ]
B = 960
print(Solution().solve(A, B))