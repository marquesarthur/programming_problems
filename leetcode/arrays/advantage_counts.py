from bisect import bisect_right

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = sorted(A)

        result = []
        for i in B:
            idx = bisect_right(A, i)
            if idx >= len(A):
                greater_than_i = A.pop(0)
            else:
                greater_than_i = A.pop(idx)
            result.append(greater_than_i)

        return result





# A = [2,7,11,15]
# B = [1,10,4,11]
# print(Solution().advantageCount(A, B))

A = [12,24,8,32]
B = [13,25,32,11]
print(Solution().advantageCount(A, B))

