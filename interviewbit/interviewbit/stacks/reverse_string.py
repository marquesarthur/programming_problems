class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        if not A:
            return None

        stack = []
        for i in range(len(A)):
            stack.append(A[i])

        result = ""
        while len(stack) > 0:
            result += str(stack.pop())

        return result
