from itertools import groupby


class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for c in S:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack += [c]
        return ''.join(stack)








i = "abbaca" # "ca"

print(Solution().removeDuplicates(i))

i = "abababaaa" # "ca"
print(Solution().removeDuplicates(i))


i = "aaaaaaa" # "a"
print(Solution().removeDuplicates(i))