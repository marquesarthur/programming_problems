import sys


class Graph(object):
    def __init__(self, n):
        self.size = n
        self.graph = [[0] * self.size] * self.size


def __min_distance_vertex(visited, dist):
    _min, u = sys.maxsize, -1
    for i in range(len(dist)):
        if dist[i] < _min and i not in visited:
            _min, u = dist[i], i

    return u

def __update_edge_distances(u, edges, dist, visited):
    for j, e in enumerate(edges):
        if e > 0 and j not in visited and dist[j] > dist[u] + e:
            dist[j] = dist[u] + e



def djikstra(graph, source, target):
    inf = sys.maxsize
    dist = [inf] * graph.size
    dist[source] = 0

    visited = set()

    while len(visited) != graph.size:
        u = __min_distance_vertex(visited, dist)
        visited.add(u)
        __update_edge_distances(u, g.graph[u], dist, visited)

    return dist[target]


g = Graph(6)
# print(g.graph)
g.graph = [
    [0, 9, 4, 0, 0, 0], # A
    [9, 0, 4, 12, 5, 0], # B
    [4, 4, 0, 0, 13, 0], # C
    [0, 12, 0, 0, 3, 2], # D
    [0, 5, 13, 3, 0, 14], # E
    [0, 0, 0, 2, 15, 0] # F
]
# print(g.graph)

print(djikstra(g, 0, 5))
print(djikstra(g, 0, 4))
