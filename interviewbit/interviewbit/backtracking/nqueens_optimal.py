def format_result(result):
    return map(lambda row: ''.join(map(lambda val: 'Q' if val == 1 else '.', row)), result)


def get_next_col(cur_col, first_row):
    for col, val in enumerate(first_row):
        if val == 1:
            return col + 1
    return cur_col + 1


def get_nqueens(cur_row, A, result, res):
    if cur_row == A:
        res.append(format_result(result))
        # return True
    else:
        for col in xrange(A):
            if not is_a_threat(cur_row, col, result, A):
                result[cur_row][col] = 1
                get_nqueens(cur_row + 1, A, result, res)
                result[cur_row][col] = 0

        # return False


def is_a_threat(row, col, result, A):
    for prev_col in xrange(col):
        if result[row][prev_col] == 1:
            return True
    for prev_row in xrange(row):
        if result[prev_row][col] == 1:
            return True

    diag_row, diag_col = row, col
    while diag_row >= 0 and diag_col >= 0:
        if result[diag_row][diag_col] == 1:
            return True
        diag_row -= 1
        diag_col -= 1

    diag_row, diag_col = row, col
    while diag_row >= 0 and diag_col < A:
        if result[diag_row][diag_col] == 1:
            return True
        diag_row -= 1
        diag_col += 1

    return False


class Solution:

    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        res = list()
        result = [[0 for _ in xrange(A)] for _ in xrange(A)]
        # col = 0
        # while col < A:
        #     result = [[0 for _ in xrange(A)] for _ in xrange(A)]
        #     if get_nqueens(0, col, A, result):
        #         res.append(format_result(result))
        #     col = get_next_col(col, result[0])
        get_nqueens(0, A, result, res)
        return res


A = [[1, 0, 0], [1, 0, 0], [0, 0, 0]]
print(Solution().solveNQueens(4))
