class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])

        row_column_pairs = []
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    row_column_pairs.append((i, j))

        processed_rows = {}
        processed_columns = {}
        for pair in row_column_pairs:
            row, column = pair

            if row not in processed_rows:
                for j in range(n):
                    A[row][j] = 0
                processed_rows[row] = True

            if column not in processed_columns:
                for i in range(m):
                    A[i][column] = 0
                processed_columns[column] = True

        return A
