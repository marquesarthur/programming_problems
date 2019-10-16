class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        easy = set()
        for i in nums:
            easy.add(i)

        for i in xrange(len(nums)):
            if i not in easy:
                return i

        return len(nums)

    def missingNumberConstantMemory(self, nums):
        """
        if we initialize an integer to nn and XOR it with every index and value,
        we will be left with the missing number.

        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing




A = [3,0,1] # 2
print(Solution().missingNumber(A))

A = [9,6,4,2,3,5,7,0,1] # 8
print(Solution().missingNumber(A))

A = [9,6,4,2,3,5,7,0,1, 8] # 10
print(Solution().missingNumber(A))