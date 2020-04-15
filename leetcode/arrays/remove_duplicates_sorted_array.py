class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []

        if len(nums) == 1:
            return nums

        i = 0
        j = 1
        unique = 1

        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                unique += 1

            j+= 1

        return nums[:unique]





a = [1,1,2]
print(Solution().removeDuplicates(a))
a = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(a))
a = [1, 2, 3, 4]
print(Solution().removeDuplicates(a))