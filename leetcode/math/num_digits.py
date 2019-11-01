
from itertools import permutations


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        count = 1
        for i in xrange(1, n + 1):
            perm = list(permutations(numbers, i))
            count += len([int("".join(t)) for t in perm if t[0] != "0"])



        return count


n = 100
# Output: 91

print(Solution().countNumbersWithUniqueDigits(n))