class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums) / 2]



# Input: 
nums = [3,2,3]
# Output: 3
print(Solution().majorityElement(nums))

# Input: 
nums = [2,2,1,1,1,2,2]
# Output: 2
print(Solution().majorityElement(nums))