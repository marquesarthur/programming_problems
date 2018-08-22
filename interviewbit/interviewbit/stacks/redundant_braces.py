class Solution:

    # (a+(a+b))
    #
    # We keep pushing elements onto the stack till we encounter ')'. When we do encounter ')', we start popping elements till we find a matching '('.
    # If the number of elements popped do not correspond to '()', we are fine and we can move forward.
    # Otherwise, voila! Matching braces have been found. 

    # @param A : string
    # @return an integer
    def braces(self, A):


        if not A:
            return 0

        stack = []
        for c in range(len(A)):
            if A[c] == "(":
                stack.append(A[c])
            elif A[c] == ")":
                pooped_elements = 0
                while stack and stack[-1] != "(":
                    stack.pop()
                    pooped_elements += 1
                stack.pop()
                if pooped_elements <= 1:
                    return 1
            else:
                stack.append(A[c])

        return 0


print(Solution().braces("((a+b))"))






