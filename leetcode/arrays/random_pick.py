import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [(i, value) for i, value in enumerate(nums)]
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        found = list(filter(lambda k: k[1] == target, self.nums))
        if found:
            if len(found) == 1:
                return found[0][0]
            else:
                return random.choice([i for i, _ in found])
        else:
            return -1
