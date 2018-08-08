#  This is the same as the KMP algorithm

class Solution:
    def init_kmp(self, A):
        idxs = [0]
        for i in range(1, len(A)):
            j = idxs[i - 1]
            while j > 0 and A[i] != A[j]:
                j -= 1
            idxs.append(j + 1 if A[i] == A[j] else j)
        return idxs

    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if not B:
            return -1

        if not A:
            return -1

        partial, ret, j = self.init_kmp(B), -1, 0

        for i in range(len(A)):
            while j > 0 and A[i] != B[j]:
                j = partial[j - 1]

            if A[i] == B[j]:
                j += 1

            if j == len(B):
                ret = i - (j - 1)
                break

        return ret
