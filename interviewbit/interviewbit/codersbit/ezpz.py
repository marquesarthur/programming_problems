import math


class Solution:

    def __is_prime(self, A):
        if A <= 1:
            return False
        for i in range(2, int(math.sqrt(A)) + 1):
            if A % i == 0:
                return False
        return True

    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A <= 1:
            return -1
        elif self.__is_prime(A):
            return 1
        elif A % 2 == 0:
            return 2
        elif A % 2 == 1 and self.__is_prime(A - 2):
            return 2
        else:
            return 3


print(Solution().solve(9))
print(Solution().solve(11))
