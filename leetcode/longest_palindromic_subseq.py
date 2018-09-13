class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        if len(s) == 1:
            return s
        
        l = len(s)
        rev = s[::-1]
        while l > 0:
            for i in range(0, len(s) - l + 1):
                half = int(l / 2)
                left = s[i: i+half]
                right = rev[len(s) - (i + l) : len(s) - (i + l - half)]
                if left == right:
                    return s[i: i + l]
            l -= 1

        return ""

