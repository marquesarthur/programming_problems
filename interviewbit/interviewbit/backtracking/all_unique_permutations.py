class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):

        # iterate over A
        # remove current idx
        # permute remaining Array
        # go over permuted array and insert idx in all indexes
        # return

        # corner case
        if not A:
            return []

        if len(A) == 1:
            return [A]



        current = A[0]
        B = A[1:len(A)]
        remaining_permutations = self.permute(B)
        result = set()
        for p in remaining_permutations:

            idxs = len(p) + 1
            for j in xrange(idxs):
                aux = list(p)
                aux.insert(j, current)
                result.add(tuple(aux))

        result = [list(r) for r in result if len(list(r)) == len(A)]
        return result


print(Solution().permute([1, 2, 3]))