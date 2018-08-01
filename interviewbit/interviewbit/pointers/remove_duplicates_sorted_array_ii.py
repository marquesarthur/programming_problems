class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):

        if not A:
            return 0

        if len(A) <= 2:
            return len(A)

        new_i = 2
        i = 2

        while i < len(A):

            if A[new_i - 2] == A[i] and A[new_i - 1] == A[i]:
                i += 1
            elif A[new_i - 2] != A[i] and A[new_i - 1] == A[i]:
                A[new_i] = A[i]
                i += 1
                new_i += 1
            elif A[new_i - 2] != A[i] and A[new_i - 1] != A[i]:
                A[new_i] = A[i]
                i += 1
                new_i += 1
            else:
                i += 1

        A = A[0:new_i + 1]
        return new_i
