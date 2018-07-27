class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if not A:
            return ""

        f = A[0]
        n = len(A)
        stack = []
        for i in range(len(f) + 1):
            preffix = f[0:i]
            longest = filter(lambda k: k.startswith(preffix), A)
            if len(longest) == n:
                stack.append(preffix)
            else:
                break

        return stack.pop()





