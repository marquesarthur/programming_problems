class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """


        output = {i: S[i] for i in range(len(S))}
        for idx, s, t in zip(indexes, sources, targets):
            init = S[idx:idx+len(s)]
            if init == s:
                output[idx] = t
                for z in range(idx + 1, idx + len(s)):
                    if z in output:
                        del output[z]

        result = []
        for i in sorted(output.keys()):
            result.append(output[i])

        return "".join(result)







# Input:

S = "abcd"
indexes = [0,2]
sources = ["a","cd"]
targets = ["eee","ffff"]
print(Solution().findReplaceString(S, indexes, sources, targets))

# Output: "eeebffff"
# Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
# "cd" starts at index 2 in S, so it's replaced by "ffff".


# Input:
S = "abcd"
indexes = [0,2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
print(Solution().findReplaceString(S, indexes, sources, targets))
# Output: "eeecd"
# Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
# "ec" doesn't starts at index 2 in the original S, so we do nothing.