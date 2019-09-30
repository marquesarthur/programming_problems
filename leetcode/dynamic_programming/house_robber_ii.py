class Solution(object):


    # Recursive solution won't pass time limit scenarios. I need a dynamic programming solution
    def helper(self, nums, idx, last_robbed, current_sum, first_idx=0):
        if len(nums) == 1:
            return nums[0]

        if idx >= len(nums):
            return current_sum

        if idx == len(nums) - 1 and first_idx == 0:
            return current_sum

        return max(
            self.helper(nums, idx + 2, idx, nums[idx] + current_sum, first_idx=first_idx), # robbing_idx
            self.helper(nums, idx + 1, last_robbed, current_sum, first_idx=first_idx) # not_robbing_idx
        )


    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self.helper(nums, 0, -1, 0, first_idx=0), self.helper(nums, 1, 0, 0, first_idx=1))


# nums = [2,3,2]
#
# print(Solution().rob(nums))
#
# nums = [1,2,3,1]
# print(Solution().rob(nums))
#
# nums = [1]
# print(Solution().rob(nums))

nums = [1,2,1,1]
print(Solution().rob(nums))