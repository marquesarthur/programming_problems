class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            if abs(nums[i]) < len(nums):
                nums[abs(nums[i])] = -nums[abs(nums[i])]

        first_missing = 0
        while first_missing < len(nums):
            if nums[first_missing] <= 0:
                first_missing += 1
            else:
                break

        return first_missing





# A = [1,2,0]
# print(Solution().firstMissingPositive(A))
#
A = [3,4,-1,1]
print(Solution().firstMissingPositive(A))
#
# A = [7,8,9,11,12]
# print(Solution().firstMissingPositive(A))