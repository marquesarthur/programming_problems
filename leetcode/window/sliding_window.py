from bisect import bisect_left

class Solution(object):

    def median(self, window, k):
        if k % 2 == 0:
            idx = int(k) / 2
            return (window[idx] + window[idx - 1]) / 2.
        else:
            return window[int(k) / 2]

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:int(k)])
        result = [self.median(window, k)]
        for i in xrange(1, len(nums) - int(k) + 1):
            last_value = nums[i - 1]
            idx = bisect_left(window, last_value)
            window.pop(idx)
            new_value = nums[i + int(k) - 1]
            idx = bisect_left(window, new_value)
            window.insert(idx, new_value)
            result.append(self.median(window, k))

        return result





nums = [1,3,-1,-3,5,3,6,7]
k = 3.

print(Solution().medianSlidingWindow(nums, k))