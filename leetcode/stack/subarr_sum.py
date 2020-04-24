
# https://leetcode.com/problems/continuous-subarray-sum/discuss/586173/Python-Prefix-Sum
class Solution:
    def checkSubarraySum(self, nums, k):
        n = len(nums) + 1
        for i in range(n):
            for j in range(n):
                aux = nums[i:j]
                if sum(aux) % k == 0 and len(aux) >= 2:
                    return True

        return False
