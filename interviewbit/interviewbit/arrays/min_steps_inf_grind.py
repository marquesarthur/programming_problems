class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        n = len(A)
        moves = 0
        for i in range(n - 1):
            ax = A[i]
            ay = B[i]

            bx = A[i + 1]
            by = B[i + 1]
            moves += self.movesBetween(ax, ay, bx, by)

        return moves

    def movesBetween(self, ax, ay, bx, by):
        x_moves = abs(bx - ax)
        y_moves = abs(by - ay)

        return max(x_moves, y_moves)
