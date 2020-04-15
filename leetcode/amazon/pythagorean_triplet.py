import math

class Solution(object):

    def __sums_up_to(self, nums, value):
        for i in nums:
            target = value - i**2
            if target > 0 and math.sqrt(target) in nums:
                return True

        return False

    def triplet(self, nums):

        # 1st sort numbers
        nums = sorted(nums) # O (n log n)
        for i, value in enumerate(nums):
            aux = nums[:i] + nums[i+1:]
            if self.__sums_up_to(set(aux), value**2):
                return True

        return False


a =  [3, 1, 4, 6, 5]
print(Solution().triplet(a))

b = [10, 4, 6, 12, 5]
print(Solution().triplet(b))