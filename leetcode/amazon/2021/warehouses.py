
import math
from collections import  defaultdict




def get_cost_of_warehouse(node, graph, visited):
    queue = []
    queue.append(node)
    n = 1
    while queue:
        n += 1
        current = queue.pop(0)
        visited.add(current)

        for child in graph[current]:
            if child not in visited:
                queue.append(child)


    return math.ceil(math.sqrt(n))







def get_cost(n, connections):

    graph = defaultdict(list)

    for i in range(n):
        graph[i] = []

    for x in connections:
        graph[x[0]].append(x[1])
        graph[x[1]].append(x[0])


    visited = set()
    total_cost = 0
    for i in range(n):
        cost = 0
        if i not in visited and len(graph[i]) == 0:
            cost = 1
            visited.add(i)
        else:
            if i not in visited:
                cost = get_cost_of_warehouse(i, graph, visited)

        total_cost += cost

    return total_cost








# cost is the ceiling of the square root of k,
# where k = number of warehouses in the group



n = 4
connections = [[0, 2], [1, 2]]
result = 3
print(get_cost(n, connections))


n = 10
connections = [
    [2, 6], [3, 5],
    [0, 1], [2, 9],
    [5, 6]
]
result = 10
print(get_cost(n, connections))