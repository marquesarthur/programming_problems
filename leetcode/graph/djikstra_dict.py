import sys




def __get_node_min_cost(dist, visited):

    min_dist, u = sys.maxint, -1
    for idx, value in enumerate(dist):
        if idx not in visited and value < min_dist:
            min_dist, u = value, idx

    return u


def __updated_costs(u, edges, dist, visited):


    for idx, edge in edges:
        if idx not in visited and edge > 0:
            if dist[idx] > edge + dist[u]:
                dist[idx] = edge + dist[u]



def djikstra(g, source, target):

    inf = sys.maxint
    dist = [inf for _ in g.keys()]
    dist[source] = 0


    visited = set()


    while len(visited) != len(g.keys()):
        u = __get_node_min_cost(dist, visited)
        visited.add(u)
        __updated_costs(u, g[u], dist, visited)



    return dist[target]




g = {
    0: [ (1, 5), (2, 2)], # A
    1: [ (0, 5), (2, 3), (3, 4)], # B
    2: [ (0, 2), (1, 3), (3, 9)], # C
    3: [ (1, 4), (2, 9)]  # D
}

print(djikstra(g, 0, 3))