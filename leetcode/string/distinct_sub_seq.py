from bisect import bisect_right

class Solution(object):

    def all_combinations_of(self, current_idx, final, partial, current_set):

        if current_idx == final:
            if len(current_set) == final:
                return 1
            else:
                return 0
        total = 0
        if not current_set:
            for valid_idx in partial[current_idx]:
                aux = list(current_set)
                aux.append(valid_idx)
                total += self.all_combinations_of(current_idx + 1, final, partial,  aux)
        else:
            last = current_set[-1]
            all_greater_than = bisect_right(partial[current_idx], last)
            for valid_idx in partial[current_idx][all_greater_than:]:
                aux = list(current_set)
                aux.append(valid_idx)
                total += self.all_combinations_of(current_idx + 1, final, partial,  aux)

        return total





    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        c_indexes = {}
        for idx, c in enumerate(s):
            if c not in c_indexes:
                c_indexes[c] = []

            c_indexes[c].append(idx)

        partial = []
        j = 0
        while j < len(t):
            if t[j] not in c_indexes:
                return 0

            partial.append(c_indexes[t[j]])

            j += 1

        # find all combinations whose index is greater than the last

        result = self.all_combinations_of(0, len(partial), partial,  [])
        return result

class SolutionOptimal(object):
    def numDistinct(self, s, t):
        n, m = len(s), len(t)
        dp = [[1 if i == 0 else 0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                sub = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    sub += dp[i - 1][j - 1]
                dp[i][j] = sub
        return dp[n][m]

#
#
S = "rabbbit"
T = "rabbit"
#
print(SolutionOptimal().numDistinct(S, T))
#
#
# S = "babgbag"
# T = "bag"
# print(Solution().numDistinct(S, T))
#
#
#
S = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
T = "bddabdcae"
print(SolutionOptimal().numDistinct(S, T))