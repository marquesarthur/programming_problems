import sys


class Graph(object):
    def __init__(self, n):
        self.size = n
        self.graph = [[0] * self.size] * self.size


def __traverse(graph, source, target, distance, solution, current_path):
    edges = graph.graph[source]
    new_path = list(current_path)
    new_path.append(source)

    if source == target:
        solution.append((distance, new_path))
    else:
        for j, e in enumerate(edges):
            if e > 0:

                __traverse(graph, j, target, distance + e, solution, new_path)



def shortest_path(graph, source, target):
    if source == target:
        return str(source)

    edges = graph.graph[source]

    distance = 0
    solution = []
    for j, e in enumerate(edges):
        if e > 0:
            __traverse(g, j, target, distance + e, solution, [source])

    distance, path = sys.maxsize, []
    for d, p in solution:
        if d < distance:
            distance, path = d, p

    return distance, " --> ".join([str(i) for i in path]) if path else "inf"




g = Graph(6)
# Direct Graph
g.graph = [
    [0, 9, 4, 0, 0, 0], # A
    [0, 0, 0, 12, 5, 0], # B
    [0, 4, 0, 0, 13, 0], # C
    [0, 0, 0, 0, 0, 2], # D
    [0, 0, 0, 3, 0, 15], # E
    [0, 0, 0, 0, 0, 0] # F
]
# print(g.graph)

print(shortest_path(g, 0, 5))
