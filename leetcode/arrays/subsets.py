class Solution(object):

    def to_set(self, result):

        aux = set([tuple(x) for x in result])
        return [list(y) for y in aux]


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return [[]]
        elif len(nums) == 1:
            return [[nums[0]], []]
        else:

            current = [nums[len(nums) - 1]]

            other_sets = self.subsets(nums[:len(nums) - 1])

            result = []
            for set in other_sets:
                result.append(list(set) + current)

            result.append(current)
            result += other_sets

            return self.to_set(result)






nums = [1,2,3]
print(Solution().subsets(nums))