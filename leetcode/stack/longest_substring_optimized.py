class Solution(object):

    def lengthOfLongestSubstring(self, s):
        seen = ''
        mx = 0
        # 1. for each character in s
        for c in s:
            # 2. check if c is seen
            if c not in seen:
                # 3. if not seen, add to seen list
                seen += c
            # 4 if seen, slice seen list to previous c
            # for example, if c is 'a' and seen list is 'abc'
            # you will be slicing previous 'a'(seen.index(c)+1), thus seen list become 'bc'
            # then add the current 'a' bc + a, seenlist = 'bca'
            else:
                seen = seen[seen.index(c) + 1:] + c
            # 5 check max length between current max with new length of seen
            mx = max(mx, len(seen))
        return mx


s = "abca"
print(Solution().lengthOfLongestSubstring(s))

s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
