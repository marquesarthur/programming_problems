class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        if not A:
            return 0

        # e.g. [2,1,5,6,2,3]
        # 2 area = 2
        # smaller than 2, base = 2 min(1, 2)
        # 5 is higher than 1 area = 1 * 5 = 5

        # I believe that I have to sort the numbers

        # A = sorted(A, reverse=True)
        # 6, 5, 3, 2, 2, 1

        stack = []
        n = len(A)
        ret = 0
        tp = -1
        area_with_top = -1
        i = 0
        while i < n:
            if len(stack) == 0 or A[i] >= A[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                area_with_top = A[tp] * (i if len(stack) == 0 else i - stack[-1] - 1)
                if ret < area_with_top:
                    ret = area_with_top
        while len(stack) != 0:
            tp = stack.pop()
            area_with_top = A[tp] * (i if len(stack) == 0 else i - stack[-1] - 1)
            if ret < area_with_top:
                ret = area_with_top

        return ret


# A = [ 90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]
# print(Solution().largestRectangleArea(A))


A = [ 4, 3, 2 ]
print(Solution().largestRectangleArea(A))