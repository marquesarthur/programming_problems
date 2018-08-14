class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):

        if B == 1:
            return A

        result = ""
        current_row = 0
        rows = [""] * B
        increasing = 1
        decreasing = -1
        order = increasing
        for i in range(len(A)):

            rows[current_row] += A[i]
            current_row += order

            if order == increasing and current_row == B:
                order = decreasing
                current_row = B - 2

            if order == decreasing and current_row == -1:
                order = increasing
                current_row = 1

        return "".join(rows)
