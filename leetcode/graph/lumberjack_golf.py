OBSTACLE = 0
GRASS = 1


class Solution(object):

    def nextMove(self, forest, position):

        n, m = len(forest), len(forest[0])
        valid_steps = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        result = []
        x, y = position
        for i, j in valid_steps:
            if 0 <= x + i < n and 0 <= y + j < m:
                if forest[x + i][y + j] != OBSTACLE:
                    result.append((x + i, y + j))

        return result

    def distance_from(self, src, trg, forest):
        visited = set()

        queue = list()
        cost_so_far = {}
        came_from = {}
        came_from[src] = None
        cost_so_far[src] = 0
        queue.append(src)

        while queue:
            current = queue.pop(0)
            visited.add(current)
            if current == trg:
                break

            for _next in self.nextMove(forest, current):
                new_cost = cost_so_far[current] + 1
                if _next not in cost_so_far or new_cost < cost_so_far[_next]:
                    cost_so_far[_next] = new_cost
                    came_from[_next] = current
                    queue.append(_next)

        if trg in cost_so_far:
            return cost_so_far[trg]
        else:
            return -1

    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """

        # You are asked to cut off all the trees in this forest in the order of tree's height -
        # always cut off the tree with lowest height first. And after cutting,
        # the original place has the tree will become a grass (value 1).

        n, m = len(forest), len(forest[0])

        trees_to_cut = []
        for i in xrange(n):
            for j in xrange(m):
                if forest[i][j] > GRASS:
                    trees_to_cut.append((forest[i][j], (i, j)))

        trees_to_cut = sorted(trees_to_cut, key=lambda k: k[0])
        current = (0, 0)
        trees_to_cut.insert(0, (0, current))

        final = 0
        for i in xrange(1, len(trees_to_cut)):
            _, src = trees_to_cut[i - 1]
            _, trg = trees_to_cut[i]

            dist = self.distance_from(src, trg, forest)
            if dist == -1:
                return dist
            else:
                final += dist

        return final


forest = [
    [1, 2, 3],
    [0, 0, 4],
    [7, 6, 5]
]

print(Solution().cutOffTree(forest))

forest = [
    [1, 1, 3],
    [1, 1, 1],
    [1, 1, 1]
]

print(Solution().cutOffTree(forest))

forest = [[1,2,3],[0,0,0],[7,6,5]]

print(Solution().cutOffTree(forest))


forest = [
    [54581641,  64080174,   24346381,   69107959],
    [86374198,  61363882,   68783324,   79706116],
    [668150,    92178815,   89819108,   94701471],
    [83920491,  22724204,   46281641,   47531096],
    [89078499,  18904913,   25462145,   60813308]
]

print(Solution().cutOffTree(forest))  # 57
