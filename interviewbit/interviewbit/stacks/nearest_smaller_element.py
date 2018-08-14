class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):

        # 34 35 27 42 5 28 39
        stack = []
        result = []
        for i, value in enumerate(A):  # 42

            if not stack:
                result.append(-1)
                stack.append(value)
                continue


            while stack and stack[-1] >= value:
                stack.pop()


            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])

            stack.append(value)

        return result


# 34 = -1
# 35 = 34
# 27 = -1
# 42


A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
A = [ 39, 27, 11, 4, 24, 32, 32, 1 ]
print(Solution().prevSmaller(A))