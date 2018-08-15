def helper(nums):
    if not nums:
        return [[]]
    else:
        first = nums[0]
        subs = helper(nums[1:])
        newl = []
        for i in subs:
            if i not in newl:
                newl.append(i)
            l = [first] + i
            if l not in newl:
                newl.append(l)
        return newl


class OptimalSolution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A.sort()
        a = helper(A)
        a.sort()
        return a

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
    def subsetsWithDup(self, A):
        result = []
        if not A:
            return [[]]

        # Adding empty set
        result.append([])

        # loop over array A
        # for each element, create a new array and also add it to previous arrays?
        self.addSubsets(result, 0, sorted(A))

        result = list(set(tuple(i) for i in result))

        return sorted([list(i) for i in result])

print(Solution().subsetsWithDup([ 6, 6, 3, 3, 6, 5 ]))