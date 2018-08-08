class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        l = 0
        r = len(A) - 1
        area = 0

        while l < r:
            # Calculating the max area
            area = max(area, min(A[l], A[r]) * (r - l))

            if A[l] < A[r]:
                l += 1
            else:
                r -= 1
        return area

s = Solution().maxArea([1, 5, 4, 3])
print(s)
