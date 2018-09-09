

def walk_through_borders(A, n, m):
    result = []
    for i in range(m):
        result.append(A[0][i])

    for i in range(1, n):
        result.append(A[i][m - 1])

    if m - 2 >= 0 and n > 1:
        for i in range(m - 2, -1, -1):
            result.append(A[n - 1][i])

    if n - 2 >= 0 and n > 1:
        for i in range(n - 2, 0, -1):
            result.append(A[i][0])

    return result



def spiral_matrix(A):
    n = len(A)
    m = len(A[0])

    result = walk_through_borders(A, n, m)
    inner_matrix = []
    for i in range(1, n - 1):

        if m - 1 > 1 and A[i][1:m-1]:
            inner_matrix.append(A[i][1:m-1])

    result = " ".join([str(i) for i in result])
    if inner_matrix:
        result += " " + spiral_matrix(inner_matrix)

    return result





A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

B = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
]

# print(spiral_matrix(A))
print(spiral_matrix(B))