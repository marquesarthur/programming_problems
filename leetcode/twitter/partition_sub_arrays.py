
from collections import Counter


class Solution():


    def solve(selfk, k, numbers):
        # corner cases
        if k == 0 or len(numbers) == 0:
            return "Yes"
        if len(numbers) % k != 0:
            return "No"

        cnt = Counter(numbers)
        for key, value in cnt.items():
            if value > len(numbers) / k:
                return "No"

        return "Yes"




print(Solution().solve(2, [1, 2, 3, 4]))
print(Solution().solve(2, [1, 2, 2, 3]))
print(Solution().solve(3, [1, 2, 2, 3]))
