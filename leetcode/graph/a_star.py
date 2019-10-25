# https://www.redblobgames.com/pathfinding/a-star/implementation.html


def get_neighbours(graph, current):
    edges = graph[current]

    result = []
    for j, e in enumerate(edges):
        if e > 0:
            result.append(j)

    return result


def breadth_first_search(graph, start):
    nodes = list()  # should behave as a queue
    nodes.append(start)

    visited = set()

    while nodes:
        current = nodes.pop(0)
        visited.add(current)

        print("Visiting: ", current)
        neighbours = get_neighbours(graph, current)
        for _next in [n for n in neighbours if n not in visited]:
            nodes.append(_next)


directed_graph = [
    [0, 1, 0, 0, 0],  # 'A': ['B'],
    [1, 0, 1, 1, 0],  # 'B': ['A', 'C', 'D'],
    [1, 0, 0, 0, 0],  # 'C': ['A'],
    [1, 0, 0, 0, 1],  # 'D': ['E', 'A'],
    [0, 1, 0, 0, 0],  # 'E': ['B']
]

# TODO
# breadth_first_search(directed_graph, 0)


WALL = -1


def get_neighbours_in_grid(grid, position):
    row, column = position

    steps = [
        (-1, 0),  # row before
        (+1, 0),  # row after
        (0, -1),  # column before
        (0, +1)  # column after
    ]

    n, m = len(grid), len(grid[0])
    valid_moves = []
    for i, j in steps:

        if 0 <= row + i < n and 0 <= column + j < m:
            if grid[row + i][column + j] != WALL:
                valid_moves.append((row + i, column + j))

    return valid_moves


def breadth_first_grid_search(grid, start, goal=None):
    nodes = list()  # should behave as a queue
    nodes.append(start)

    visited = set()

    while nodes:
        current = nodes.pop(0)
        visited.add(current)

        if goal and current == goal:
            print("Visiting: ", current)
            break  # required for greedy best first search and A*

        print("Visiting: ", current)
        neighbours = get_neighbours_in_grid(grid, current)
        for _next in [n for n in neighbours if n not in visited]:
            nodes.append(_next)


grid_w_walls = [
    [0, 0, 0, 0, 0, 0, -1],
    [0, 0, 0, -1, 0, 0, 0],
    [0, 0, -1, 0, -1, 0, 0],
    [-1, 0, -1, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0],
]

print(breadth_first_grid_search(grid_w_walls, (0, 0)))
print(breadth_first_grid_search(grid_w_walls, (0, 0), goal=(3, 3)))


import heapq

class PriorityQueue(object):

    def __init__(self):
        self.elements = []

    def empty(self):
        if not self.elements:
            return True
        return False


    def push(self, item, cost):
        heapq.heappush(self.elements, (cost, item))



    def pop(self):
        return heapq.heappop(self.elements)



import sys

def djikstra_grid_search(grid, start, goal=None):
    nodes = PriorityQueue()
    nodes.push(start, 0)

    visited = set()
    cost_so_far = {}
    came_from = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while nodes:
        _, current = nodes.pop()
        visited.add(current)

        if goal and current == goal:
            print("Visiting: ", current)
            break  # required for greedy best first search and A*

        print("Visiting: ", current)
        neighbours = get_neighbours_in_grid(grid, current)

        for _next in neighbours:
            x, y = _next
            new_cost = cost_so_far[current] + grid[x][y]
            if _next not in cost_so_far or new_cost < cost_so_far[_next]:
                cost_so_far[_next] = new_cost
                priority = new_cost
                nodes.push(_next, priority)
                came_from[_next] = current

    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path



# this graph here: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
graph = [
    [3, 1, 5, 6],
    [8, 2, 7, 8],
    [1, 1, 8, 2]
]

came_from, cost_so_far = djikstra_grid_search(graph, (0,0), (2, 3))
print(reconstruct_path(came_from, (0,0), (2, 3)))