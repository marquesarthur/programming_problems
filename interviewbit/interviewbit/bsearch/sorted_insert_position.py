from bisect import bisect_right as upper_bound

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        if not A:
            return 0

        idx = upper_bound(A, B) - 1
        if A[idx] == B:
            return idx
        else:
            return idx + 1


A =  [1,3,5,6]
print(Solution().searchInsert(A, 5))
print(Solution().searchInsert(A, 2))
print(Solution().searchInsert(A, 7))
print(Solution().searchInsert(A, 0))
print(Solution().searchInsert([], 0))
