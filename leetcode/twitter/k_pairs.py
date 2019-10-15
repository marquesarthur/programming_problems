from collections import defaultdict


class Solution():

    def kNonRepeatedPairs(self, A, k):

        aux = defaultdict(list)

        A = sorted(A)

        for i, a in enumerate(A):
            aux[a].append(i)

        pairs = set()
        for a in A:
            target = a + k
            if target in aux and a in aux:
                aux[target].pop()
                aux[a].pop()

                pair = (a, target)
                pairs.add(tuple(sorted(pair)))

                if not aux[target]:
                    del aux[target]

                if not aux[a]:
                    del aux[a]

        return len(pairs)

    def kPairs(self, A, k):

        aux = defaultdict(list)

        A = sorted(A)

        for i, a in enumerate(A):
            aux[a].append(i)

        pairs = set()
        for a in A:
            target = a + k
            if target in aux and a in aux:

                pair = (a, target)
                if a == target and len(aux[target]) >= 2:
                    pairs.add(tuple(sorted(pair)))
                elif a != target:

                    pairs.add(tuple(sorted(pair)))

        return len(pairs)


A, k = [3, 1, 4, 1, 5], 2

print(Solution().kPairs(A, k))

A, k = [1, 2, 3, 4, 5], 1
print(Solution().kPairs(A, k))

A, k = [1, 3, 1, 5, 4], 0
print(Solution().kPairs(A, k))
