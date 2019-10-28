def compare(a, b):
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))

    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        result = sorted(nums, cmp=compare, reverse=True)

        while result and result[0] == 0 and len(result) > 1:
            result.pop(0)

        return "".join([str(k) for k in result])


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))

nums = []
print(Solution().largestNumber(nums))

nums = [0, 0]
print(Solution().largestNumber(nums))
