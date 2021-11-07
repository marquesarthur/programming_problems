from bisect import bisect_left

class Solution():

    def findPair(self, nums, target):

        new_target = target - 30

        nums = [(idx, value) for idx, value in enumerate(nums)]

        nums = sorted(nums, key=lambda k: k[1])
        values = [n[1] for n in nums]

        j = len(nums) - 1
        while j >= 0:
            lookup = new_target - values[j]
            idx = bisect_left(values, lookup)

            if values[idx] == lookup:
                return [nums[idx][0], nums[j][0]]

            j -= 1

        return []


nums = [1, 10, 25, 35, 60]
target = 90

print(Solution().findPair(nums, target))

nums = [20, 50, 40, 25, 30, 10]
target = 90
print(Solution().findPair(nums, target))