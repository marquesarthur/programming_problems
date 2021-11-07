class Sailing(object):

    def __init__(self, map):
        self.map = map
        self.visited = []
        self.queue = [(0, 0)] # start

        self.safe = 'O'
        self.rock = 'D'
        self.treasure = 'X'

        self.n = len(self.map)
        self.m = len(self.map[0])
        self.min_path = self.m * self.n

    def find_path(self):


        queue = []

        queue.append((0, 0))

        steps = 0
        visited = set()
        visited.add((0, 0))
        while queue:
            k = len(queue)
            for _ in range(k):
                current = queue.pop(0)

                i, j = current
                if self.map[i][j] == self.treasure:
                    return steps

                next = self.get_next(i, j)

                for next_i, next_j in next:
                    if (next_i, next_j) not in visited:
                        if self.map[next_i][next_j] != self.rock:
                            queue.append((next_i, next_j))
                            visited.add((next_i, next_j))

            steps += 1

        return steps







    def get_next(self, i, j):
        result = []
        # up
        if j - 1 >= 0:
            result.append((i, j - 1))
        # down
        if j + 1 < self.m:
            result.append((i, j + 1))
        # left
        if i - 1 >= 0:
            result.append((i - 1, j))
        # right
        if i + 1 < self.n:
            result.append((i + 1, j))

        return result


def find_treasure(input):
    kid = Sailing(input)
    result = kid.find_path()
    return result


input = [
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'O', 'D', 'O']
]

print(find_treasure(input))
