class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        n = len(board)
        for i in range(n):
            row = [r for r in board[i] if r != "."]
            if len(row) != len(set(row)):
                return False

            column = []
            for j in range(n):
                column.append(board[j][i])

            column = [c for c in column if c != "."]
            if len(column) != len(set(column)):
                return False

        for i in range(0, n, 3):

            for j in range(0, n, 3):
                square = []
                square += board[i][j:j + 3]
                square += board[i + 1][j:j + 3]
                square += board[i + 2][j:j + 3]

                square = [c for c in square if c != "."]
                if len(square) != len(set(square)):
                    return False

        return True

A = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(A))

A = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(A))