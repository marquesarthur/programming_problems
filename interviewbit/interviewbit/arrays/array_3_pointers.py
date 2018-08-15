class Solution:
    def max_func(self, a, b, c):
        return max(abs(a - b), abs(b - c), abs(c - a))

    def increment_pointers(self, i, j, k, a, b, c):
        _min = min(a, b, c)

        if _min == a:
            return i + 1, j, k
        elif _min == b:
            return i, j + 1, k
        else:
            return i, j, k + 1

    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):

        A = list(A)
        B = list(B)
        C = list(C)

        i, j, k = 0, 0, 0
        _min = self.max_func(A[-1], B[-1], C[-1])

        while i < len(A) and j < len(B) and k < len(C):
            a, b, c = A[i], B[j], C[k]
            _min = min(_min, self.max_func(a, b, c))
            i, j, k = self.increment_pointers(i, j, k, a, b, c)

        return _min
