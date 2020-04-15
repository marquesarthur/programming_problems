class Solution(object):

    def nearest_zero(self, matrix, i, j, m, n):

        queue = []
        queue.append((i, j, 0))
        visited = []

        N = n * m

        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue and len(visited) < N:
            x, y, distance = queue.pop(0)
            visited.append((x, y))
            if matrix[x][y] == 0:
                return distance

            for j, k in neighbours:
                if 0 <= x + j < n and 0 <= y + k < m:
                    if (x + j, y + k) not in visited:
                        queue.append((x + j, y + k, distance + 1))


        return -1









    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])

        out = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                out[i][j] = self.nearest_zero(matrix, i, j, m, n)

        return out


# Input:
# A = [
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]
# ]
# output = Solution().updateMatrix(A)
# for i in output:
#     print(i)
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]


# Input:
A = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

# Output:
# [[0, 0, 0],
#  [0, 1, 0],
#  [1, 2, 1]]
print("-----")
output = Solution().updateMatrix(A)
for i in output:
    print(i)