class Solution:

    def binSearch(self, A, target, start, end):
        while (start <= end):
            mid = int((start + end) / 2)
            if A[mid][1] == target:
                return A[mid][0]
            elif A[mid][1] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if not nums:
            return result

        nums = sorted([(i, x) for i, x in enumerate(nums)], key=lambda k: k[1])
        for k in nums:
            i, x = k
            y = target - x
            j = self.binSearch(nums, y, 0, len(nums) - 1)

            if j != i and j != -1 and not result:
                result = sorted([i, j])
                break

        return result


print(Solution().twoSum([3, 2, 3], 6))
