import sys


class Graph(object):
    def __init__(self, n):
        self.size = n
        self.graph = [[0] * self.size] * self.size


def __min_distance_vertex(dist, visited):
    u, _min = None, sys.maxsize

    for v, d in enumerate(dist):
        if d < _min and v not in visited:
            u, _min = v, d

    return u


def djikstra(graph, source, target):
    inf = sys.maxsize
    dist = [inf] * graph.size
    dist[source] = 0
    visited = set()
    path = list()
    path.append(source)

    while len(visited) != graph.size:
        u = __min_distance_vertex(dist, visited)
        visited.add(u)


        edges = graph.graph[u]

        for j, e in enumerate(edges):
            if e > 0 and j not in visited and dist[j] > dist[u] + e:
                dist[j] = dist[u] + e

    return dist[target], path


g = Graph(6)
# print(g.graph)
g.graph = [
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 1, 1, 1, 0],  # B
    [1, 1, 0, 0, 1, 0],  # C
    [0, 1, 0, 0, 1, 1],  # D
    [0, 1, 1, 1, 0, 1],  # E
    [0, 0, 0, 1, 1, 0]  # F
]

print(djikstra(g, 0, 5))