import sys



def __get_node_with_min_cost(visited, dist_from_source_to):
    min_dist, u = sys.maxint, -1

    for idx, node in enumerate(dist_from_source_to):
        if idx not in visited and node < min_dist:
            min_dist, u = node, idx

    return u



def __update_edge_distances(node, edges, dist_from_source_to, visited):

    for idx, edge in enumerate(edges):
        if edge > 0 and idx not in visited:
            if dist_from_source_to[node] + edge < dist_from_source_to[idx]:
                dist_from_source_to[idx] = dist_from_source_to[node] + edge


def djikstra(graph, source, target):

    inf = sys.maxint
    visited = set()

    dist_from_source_to = [inf for _ in xrange(len(graph))]
    dist_from_source_to[source] = 0

    while len(visited) != len(graph):
        u = __get_node_with_min_cost(visited, dist_from_source_to)
        visited.add(u)
        __update_edge_distances(u, graph[u], dist_from_source_to, visited)

    return dist_from_source_to[target]









g = [
    [0, 5, 2, 0], # A
    [5, 0, 3, 4], # B
    [2, 3, 0, 9], # C
    [0, 4, 9, 0]  # D
]

print(djikstra(g, 0, 3))