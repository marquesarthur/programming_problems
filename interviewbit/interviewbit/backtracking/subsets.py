class Solution:
    def addSubsets(self, result, i, A):
        if i >= len(A):
            return

        partial = []
        for j in range(len(result)):
            aux = list(result[j])
            aux.append(A[i])
            partial.append(aux)

        result += partial
        self.addSubsets(result, i + 1, A)

    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        result = []
        if not A:
            return [[]]

        # Adding empty set
        result.append([])

        # loop over array A
        # for each element, create a new array and also add it to previous arrays?
        self.addSubsets(result, 0, sorted(A))

        # result = list(set(tuple(i) for i in result))

        # return sorted([list(i) for i in result])
        return sorted(result)


print(Solution().subsets([12, 13]))
