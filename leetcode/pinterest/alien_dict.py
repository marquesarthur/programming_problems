from collections import defaultdict


class Solution():

    def alienDict(self, _in):

        max_j = max([len(k) for k in _in])
        letters = defaultdict(list)
        for i in xrange(max_j):
            for w in _in:
                if i < len(w):
                    letters[i].append(w[i])

        order = []
        # for each letter it must always appear in a group if it appears again later the dict is not valid
        for i in xrange(max_j):
            ws = letters[i]
            seen = list()
            seen.append(ws[0])
            for i in xrange(1, len(ws)):
                if ws[i] != ws[i - 1]:  # found a new letter
                    if ws[i] not in seen:
                        seen.append(ws[i])
                    elif ws[i] not in order:
                        return ""

            order += [s for s in seen if s not in order]

        return "".join(order)


# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.
#
_in = [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]

_out = "wertf"
print(Solution().alienDict(_in))
#
_in = [
    "z",
    "x"
]

_out = "zx"
print(Solution().alienDict(_in))

_in = [
    "z",
    "x",
    "z"
]

_out = ""  # invalid
print(Solution().alienDict(_in))
