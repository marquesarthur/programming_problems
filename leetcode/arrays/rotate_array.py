class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 1:
            return nums

        if k > len(nums):
            k = k % len(nums)

        # a = nums[-k:]
        # b = nums[0:len(nums) - k]
        #
        # return a + b

        for i in range(k): # in-place O(1)
            nums.insert(0, nums.pop())

        return nums


a =  [1,2,3,4,5,6,7]
k = 3
# [5,6,7,1,2,3,4]
print(Solution().rotate(a, k))
#
a = [-1,-100,3,99]
k = 2
#  [3,99,-1,-100]
print(Solution().rotate(a, k))