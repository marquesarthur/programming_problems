class Solution:

    def __diagonals(self, A, i, j):
        upper, lower = True, True
        k, l = i, j
        while k < len(A) and l < len(A):
            if A[k][l] == 1:
                upper = False
                break
            k += 1
            l += 1


        if upper:
            k, l = i - 1, j - 1
            while k >= 0 and l >= 0:
                if A[k][l] == 1:
                    upper = False
                    break
                k -= 1
                l -= 1



        k, l = i, j
        while k >= 0 and l < len(A):
            if A[k][l] == 1:
                lower = False
                break
            k -= 1
            l += 1

        if lower:
            k, l = i + 1, j - 1
            while k < len(A) and l >= 0:
                if A[k][l] == 1:
                    lower = False
                    break
                k += 1
                l -= 1

        return upper, lower

    def __can_add_queen(self, A, i, j):
        row = sum(A[i]) == 0
        if not row:
            return False
        column = sum([A[k][j] for k in xrange(len(A))]) == 0
        if not column:
            return False
        upper_diagonal, lower_diagonal = self.__diagonals(A, i, j)

        return row and column and upper_diagonal and lower_diagonal


    def __solve_queens(self, M, i, j, A, solutions):
        if i == j == A - 1:
            _sum = 0
            for row in M:
                _sum += sum(row)

            if _sum == A:
                solutions.append(M)

            return
        elif i >= A and j < A:
            return
        else:
            if self.__can_add_queen(M, i, j):
                N = [row[:] for row in M]
                N[i][j] = 1

                if j == A - 1:
                    self.__solve_queens(N, i + 1, 0, A, solutions)
                else:
                    self.__solve_queens(N, i, j + 1, A, solutions)

            if j == A - 1:
                self.__solve_queens(M, i + 1, 0, A, solutions)
            else:
                self.__solve_queens(M, i, j + 1, A, solutions)

    def __to_string(self, solutions):
        result = []
        for s in solutions:
            partial = []
            for row in s:
                partial.append("".join(["Q" if r == 1 else "." for r in row]))

            result.append(partial)

        return result


    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        if A < 4:
            return []
        M = [[0] * A] * A
        solutions = []
        self.__solve_queens(list(M), 0, 0, A, solutions)
        return self.__to_string(solutions)





# create matrice of 0s of size AxA
# for each position in the array make a solution adding a queen in that
# position and also not adding the queen
#   IFF possible
# when you reach A, stop
# convert 0s and 1s to approppriate format
# return





A = [[1, 0, 0], [1, 0, 0], [0, 0, 0]]

print(Solution().solveNQueens(4))
# print(Solution().can_add_queen(A, 1, 2))