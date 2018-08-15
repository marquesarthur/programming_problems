# Couting sort
class OptimalSolution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        B = [0,0,0]
        for i in A:
            B[i] += 1
        return [0]*B[0] + [1]*B[1] + [2]*B[2]


class Solution:
    def merge(self, A, B):
        i, j = 0, 0
        result = []

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1

        while i < len(A):
            result.append(A[i])
            i += 1

        while j < len(B):
            result.append(B[j])
            j += 1

        return result

    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        if not A:
            return A

        if len(A) == 1:
            return A

        # how different is that from a merge sort?

        start = 0
        end = len(A)
        mid = int((start + end) / 2)

        B = self.sortColors(A[0:mid])
        C = self.sortColors(A[mid:len(A)])

        result = self.merge(B, C)
        return result
