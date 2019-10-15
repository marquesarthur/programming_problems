

class Node():

    def __init__(self, i, j):
        self.children = []
        self.i = i
        self.j = j
        self.visited = False


class Solution():

    def treasure(self, M):
        # Build adj list for coordinates
        from collections import defaultdict
        d = defaultdict(list)
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] != 'D':
                    # no need to store the link the other way around. It's done implcity due to looping over cells
                    if i + 1 <= len(M) - 1:
                        d[(i, j)].append((i + 1, j))
                    if i - 1 >= 0:
                        d[(i, j)].append((i - 1, j))
                    if j + 1 <= len(M[i]) - 1:
                        d[(i, j)].append((i, j + 1))
                    if j - 1 >= 0:
                        d[(i, j)].append((i, j - 1))

        # BFS
        from collections import deque
        q = deque()
        q.append((0, 0))  # top-left = start
        steps = 0
        visited = set()
        while q:
            for i in range(len(q)):
                node = q.popleft()  # node = (x,y)

                if M[node[0]][node[1]] == 'X':
                    return steps

                for n in d[node]:
                    if n not in visited:
                        if M[n[0]][n[1]] != 'D':  # safe to sail or if lucky treasure
                            q.append((n))
                            visited.add(n)
                            d[n].remove(node)
                del d[node]
            steps += 1
        return steps


# create graph
# run breadth first search


input = [
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O']
]


expected = 5

print(Solution().treasure(input))