class Solution:
    def opposite(self, left, right):
        mtx = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        if left not in mtx:
            return False

        return right == mtx[left]

    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack = []
        left_parenthesis = ["(", "{", "["]
        right_parenthesis = [")", "}", "]"]

        for i in range(len(A)):
            if A[i] in left_parenthesis:
                stack.append(A[i])
            else:
                if not stack:
                    return 0

                last = stack.pop()
                if not self.opposite(A[i], last):
                    return 0

        return int(len(stack) == 0)
