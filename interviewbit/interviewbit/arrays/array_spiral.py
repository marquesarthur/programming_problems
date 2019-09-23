


def spiral(n):
    out = [[0 for j in range(n)] for i in range(n)]


    k = 0
    l = 0
    m = n

    current = 1
    while k < m and l < n:
        # walk left
        for j in range(l, n):
            out[k][j] = current
            current += 1

        k += 1

        # walk south
        for i in range(k, m):
            out[i][n - 1] = current
            current += 1

        n -= 1

        if (k < m):
            for j in range(n - 1, l - 1, -1):
                out[m - 1][j] = current
                current += 1

            m -= 1

        if (l < n):
            for i in range(m - 1, k - 1, -1):
                out[i][l] = current
                current += 1

            l += 1

    return out





y = spiral(4)
for i in range(len(y)):
    out = " ".join([str(x) for x in y[i]])
    print(out)