class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if not A:
            return []

        if len(A) == 1:
            return [A]

        # remove index i from array
        # get all permutations for subarrays of i
        # re-insert i in all positions
        # return
        result = []
        i = 0

        B = A[i + 1:len(A)]
        inner_permutations = self.permute(B)
        for partial in inner_permutations:
            # insert at all possible indexes
            for j in range(len(partial) + 1):
                aux = list(partial)
                aux.insert(j, A[i])
                result.append(aux)

        return sorted(result)

print(Solution().permute([1, 2, 3]))






