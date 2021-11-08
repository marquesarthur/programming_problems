from collections import Counter, defaultdict


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        most_frequent = Counter(words).most_common()

        aux = defaultdict(list)
        __min = 0

        for w, _k in most_frequent:
            __min = max(__min, _k)
            aux[_k].append(str(w))

        result = []
        for key in sorted(aux.keys(), reverse=True):
            result += sorted(aux[key], key=str.lower)
            if len(result) > k:
                break

        return result[:k]


print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
