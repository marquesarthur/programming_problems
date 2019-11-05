import sys


class Solution(object):

    def __peaks(self, nums, i, j, peaks):
        if i > j:
            return

        mid = (i + j) / 2

        left = -sys.maxint - 1 if mid - 1 < 0 else nums[mid - 1]
        right = -sys.maxint - 1 if mid + 1 >= len(nums) else nums[mid + 1]

        if left < nums[mid] > right:
            peaks.append(mid)
        elif i != j:
            self.__peaks(nums, i, mid, peaks)
            self.__peaks(nums, mid + 1, j, peaks)

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = len(nums) - 1

        peaks = []
        self.__peaks(nums, i, j, peaks)
        return peaks.pop()


nums = [5, 1, 9] # 2
print(Solution().findPeakElement(nums))

#
# nums = [1,2,3,1] # 2
# print(Solution().findPeakElement(nums))
#
# nums = [1,2,1,3,5,6,4] # 1 or 5
# print(Solution().findPeakElement(nums))