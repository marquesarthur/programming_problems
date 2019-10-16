class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """


        letters_in_magazine = {}


        for c in magazine:
            if c not in letters_in_magazine:
                letters_in_magazine[c] = 0
            letters_in_magazine[c] += 1


        for c in ransomNote:
            if c not in letters_in_magazine:
                return False

            if letters_in_magazine[c] <= 0:
                return False

            letters_in_magazine[c] -= 1


        return True

print(Solution().canConstruct("a", "b") ) #-> false
print(Solution().canConstruct("aa", "ab") )#-> false
print(Solution().canConstruct("aa", "aab")) #-> true