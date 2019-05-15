class Solution:

    def bin_search_min(self, nums, target, start, end):
        if start <= end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                idx = mid
                _next = self.bin_search_min(nums, target, start, mid - 1)
                if _next != -1:
                    return min(idx, _next)
                else:
                    return idx
            elif nums[mid] < target:
                return self.bin_search_min(nums, target, mid + 1, end)
            else:
                return self.bin_search_min(nums, target, start, mid - 1)

        return -1

    def bin_search_max(self, nums, target, start, end):
        if start <= end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                idx = mid
                _next = self.bin_search_max(nums, target, mid + 1, end)
                if _next != -1:
                    return max(idx, _next)
                else:
                    return idx
            elif nums[mid] < target:
                return self.bin_search_max(nums, target, mid + 1, end)
            else:
                return self.bin_search_max(nums, target, start, mid - 1)

        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _min_idx = self.bin_search_min(nums, target, 0, len(nums) - 1)
        _max_idx = self.bin_search_max(nums, target, 0, len(nums) - 1)

        return [_min_idx, _max_idx]

nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(Solution().searchRange(nums, target))