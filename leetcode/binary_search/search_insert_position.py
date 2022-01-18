class Solution(object):

    def binarySearch(self, nums, target, i, j):

        if i <= j:

            mid = (i + j) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binarySearch(nums, target, i, mid - 1)
            elif nums[mid] < target:
                return self.binarySearch(nums, target, mid + 1, j)

        else:
            return i


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, target, 0, len(nums) - 1)
        

        


# Example 1:

# Input: 
nums = [1,3,5,6]
target = 5
print(Solution().searchInsert(nums, target))
# Output: 2

# Example 2:

# Input: 
nums = [1,3,5,6]
target = 2
print(Solution().searchInsert(nums, target))
# Output: 1

# Example 3:

# Input: 
nums = [1,3,5,6]
target = 7
print(Solution().searchInsert(nums, target))
# Output: 4
