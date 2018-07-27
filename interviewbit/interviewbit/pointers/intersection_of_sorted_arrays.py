class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        if not B or not A:
            return []

        B = [i for i in B]

        idx_b = 0
        result = []
        for i in range(len(A)):
            while idx_b < len(B) and B[idx_b] < A[i]:
                idx_b += 1

            if idx_b < len(B) and B[idx_b] == A[i]:
                result.append(A[i])
                idx_b += 1

        return result


# Not fast enough
class BinarySearchSolution:
    def binary_search(self, B, value):
        first = 0
        last = len(B) - 1
        found = False
        idx = -1
        while first <= last and idx == -1:
            mid = (first + last) / 2

            if B[mid] == value:
                idx = mid
            else:
                if value < B[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return idx

    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        if not B or not A:
            return []

        B = [i for i in B]
        result = []
        for i in range(len(A)):
            a = A[i]
            idx_in_B = self.binary_search(B, a)
            if idx_in_B != -1:
                result.append(a)
                del B[idx_in_B]

        return result
