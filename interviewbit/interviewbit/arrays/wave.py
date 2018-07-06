


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A = sorted(A)
        for i in range(0, len(A), 2):
            if i + 1 < len(A):
                ai = A[i]
                ai_plus_1 = A[i+1]
                A[i] = ai_plus_1
                A[i + 1] = ai

        return A

