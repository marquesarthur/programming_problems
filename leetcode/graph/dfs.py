def build_graph(input):
    from collections import defaultdict

    graph = defaultdict(list)

    n = len(input)
    m = len(input[0])

    for node, i in enumerate(range(n)):
        for to, j in enumerate(range(m)):
            edge = input[i][j]
            if edge > 0:
                graph[node].append((to, edge))
    return graph


def depth_first(graph, start, end):
    """
        this is similar to bfs. Queue is replaced by a stack
    """

    queue = []
    visited = set()

    queue.append((start, 0))

    breadth_first_path = -1
    while queue and len(visited) < len(graph.keys()):

        current_node, current_path = queue.pop()
        print("visiting %s" % (current_node,))

        if current_node == end:
            breadth_first_path = current_path
            break

        visited.add(current_node)


        neighbours = graph[current_node]
        for n in neighbours:
            node, edge = n
            if node not in visited:
                queue.append((node, current_path + edge))

    return breadth_first_path


input = [
    #    A  B  C  D  E
    [0, 9, 4, 0, 0],  # A
    [0, 0, 12, 0, 5],  # B
    [0, 4, 0, 2, 0],  # C
    [1, 0, 0, 15, 0],  # D
    [0, 0, 3, 0, 0],  # E
]

graph = build_graph(input)

# path from 0 to 3 = 6
# path = depth_first(graph, 0, 3)
# print(path)
#
# # path from 0 to 1 = 9
path = depth_first(graph, 1, 0)
print(path)
#
# # path from 1 to 0 = 15
# path = depth_first(graph, 1, 0)
# print(path)
