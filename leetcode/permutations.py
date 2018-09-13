class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        to_be_permuted = nums[0]
        permuted = self.permute(nums[1:len(nums)])

        result = set()
        if not permuted:
            result.add(tuple([to_be_permuted]))
        else:
            for l in permuted:
                for i in range(0, len(l) + 1):
                    k = list(l)
                    k.insert(i, to_be_permuted)

                    result.add(tuple(k))

        result = sorted(result)
        return [list(i) for i in result]



print(Solution().permute([1, 2, 3]))