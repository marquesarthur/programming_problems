from collections import Counter


class Solution:

    def count_vowels(self, s):
        c = Counter(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        for v in vowels:
            if v in c and c[v] % 2 != 0:
                return False
        return True


    def findTheLongestSubstring(self, s):
        n = len(s) + 1
        result = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(0, n):
            for j in range(i, n):

                sub_str = s[i:j]
                vowels = self.count_vowels(sub_str)

                aux = 0
                if vowels:
                    aux = len(sub_str)
                if i - 1 >= 0:
                    aux = max(result[i-1][j], aux)
                if j - 1 >= 0:
                    aux = max(result[i][j-1], aux)

                    result[i][j] = aux
        return result[n-1][n-1]





# print(Solution().findTheLongestSubstring("eleetminicoworoep"))
print(Solution().findTheLongestSubstring("bcbcbc"))