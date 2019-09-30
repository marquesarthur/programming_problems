import itertools


class Solution(object):
    """
        2 Pointer
    """

    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        j = 0

        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(name)


class Solution2(object):
    """
    group it into blocks groupify(S) = [('a', 2), ('b', 4), ('c', 3)], that consist of a key 'abc' and a count [2, 4, 3].

    Then, the necessary and sufficient condition for typed to be a long-pressed version of name is that the keys are the same,
    and each entry of the count of typed is at least the entry for the count of name.

    'aaleex' is a long-pressed version of 'alex': because when considering the groups
        g1 = [('a', 1), ('l', 1), ('e', 1), ('x', 1)]
        g2 = [('a', 2), ('l', 1), ('e', 2), ('x', 1)]

        all(k1 == k2 and v1 <= v2 for (k1,v1), (k2,v2) in zip(g1, g2))
    """

    def isLongPressedName(self, name, typed):
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))


name = "alex"
typed = "aaleex"
print(Solution().isLongPressedName(name, typed))

name = "saeed"
typed = "ssaaedd"
print(Solution2().isLongPressedName(name, typed))

name = "leelee"
typed = "lleeelee"
print(Solution().isLongPressedName(name, typed))

name = "laiden"
typed = "laiden"
print(Solution().isLongPressedName(name, typed))
