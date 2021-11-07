from collections import Counter
import functools


def compare(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return 1
        else:
            return -1
    else:
        return 1


class Solution:
    def topKFrequent(self, words, k):
        if not words:
            return []

        c = Counter(words)
        result = c.most_common()

        result = sorted(result, key=functools.cmp_to_key(compare), reverse=True)
        return [c[0] for c in result[:k]]
