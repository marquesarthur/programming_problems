class Solution:
    def decrease_idxs(self, idx_a, idx_b, idx_c, a, b, c):
        _max = max(a, b, c)
        if _max == a:
            return idx_a - 1, idx_b, idx_c
        elif _max == b:
            return idx_a, idx_b - 1, idx_c
        else:
            return idx_a, idx_b, idx_c - 1

    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):

        idx_a, idx_b, idx_c = len(A) - 1, len(B) - 1, len(C) - 1

        a, b, c = A[idx_a], B[idx_b], C[idx_c]

        min_diff = abs(max(a, b, c) - min(a, b, c))

        while idx_a >= 0 and idx_b >= 0 and idx_c >= 0:
            a, b, c = A[idx_a], B[idx_b], C[idx_c]

            current_diff = abs(max(a, b, c) - min(a, b, c))

            if current_diff < min_diff:
                min_diff = current_diff

            idx_a, idx_b, idx_c = self.decrease_idxs(idx_a, idx_b, idx_c, a, b, c)

        return min_diff

