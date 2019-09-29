class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        if n == 0:
            return 0
        if n == 1:
            return 1

        stack = [s[0]]

        for i in range(1, n):
            current = s[i]

            # To check if a character is already in the substring, we can scan the substring, which leads to an O(n^2) algorithm. But we can do better.
            # If we change the solution to a hashmap

            if current not in stack[-1]:
                tp = stack.pop()
                stack.append(tp + current)
            else:
                tp = stack.pop()
                stack.append(tp)
                stack.append(tp[tp.index(current) + 1:] + current)

        longest = 1
        while(stack):
            tp = stack.pop()
            longest = max(longest, len(tp))

        return longest




s = "abca"
print(Solution().lengthOfLongestSubstring(s))

s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
