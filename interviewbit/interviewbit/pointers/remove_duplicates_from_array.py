class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        if len(A) <= 1:
            return len(A)

        new_i = 1
        i = 1
        while i < len(A):

            if A[new_i - 1] == A[i]:
                i += 1
            else:
                A[new_i] = A[i]
                new_i += 1

        A = A[0:new_i]
        return new_i
