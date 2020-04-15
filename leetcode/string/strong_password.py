import re


class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        MIN_LENGTH = 6
        MAX_LENGTH = 20

        if not s:
            return 0

        if len(s) < MIN_LENGTH:
            return 0

        if len(s) > MAX_LENGTH:
            return 0

        if not re.findall("[a-z]", s): # at least one lowercase letter
            return 0

        if not re.findall("[A-Z]", s): # at least one uppercase letter
            return 0

        if not re.findall("[0-9]", s): # at least one digit
            return 0

        # check consecutive characters
        if re.findall("([a-z\\d])\\1\\1", s.lower()):
            return 0

        return 1



    # It has at least 6 characters and at most 20 characters.
    # It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
    # It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

print(Solution().strongPasswordChecker("aaa1bbb2De999"))
print(Solution().strongPasswordChecker("AA1DeF43"))
print(Solution().strongPasswordChecker("A1bc2D34e"))
# print(Solution().strongPasswordChecker("aaaa"))
# print(Solution().strongPasswordChecker("aaaa"))
# print(Solution().strongPasswordChecker("aaaa"))
# print(Solution().strongPasswordChecker("aaaa"))