from collections import defaultdict
import sys
import random

inf = sys.maxint


class Graph(object):

    def __init__(self, n):
        self.n = n
        self.nodes = defaultdict(list)
        # initialize graph
        for i in range(n):
            self.nodes[i] = list()
        self.dist_from_source_to = [inf for _ in range(n)]

    def update_graph(self, times):
        for _from, _to, _cost in times:
            _from, _to = _from -1, _to -1
            self.nodes[_from].append((_to, _cost))

    def __get_node_min_cost(self, visited):
        min_dist, node = inf, -1
        for idx, current in enumerate(self.dist_from_source_to):
            if idx not in visited and current < min_dist:
                min_dist = current
                node = idx

        if node == -1:
            aux = [i for i in range(self.n) if i not in visited]
            return random.choice(aux)

        return node

    def __update_edge_propagation_time(self, node, edges, visited):
        for _to, cost in edges:
            if _to not in visited and cost > 0:
                if self.dist_from_source_to[node] + cost < self.dist_from_source_to[_to]:
                    self.dist_from_source_to[_to] = self.dist_from_source_to[node] + cost

    def djikstra(self, k):
        visited = set()
        self.dist_from_source_to[k] = 0
        while len(visited) != self.n:
            # find node in graph not visited which has the edge with min propagation time
            next_node = self.__get_node_min_cost(visited)
            visited.add(next_node)
            # check if the sum for the current node is small than the total 
            self.__update_edge_propagation_time(next_node, self.nodes[next_node], visited)


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        k = k -1
        g = Graph(n)
        g.update_graph(times)
        g.djikstra(k)

        prop_time = -1
        for idx, value in enumerate(g.dist_from_source_to):
            if idx != k:
                prop_time = max(prop_time, value)

        if prop_time == inf:
            prop_time = -1

        return prop_time


# times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
# n = 4
# k = 2
# # Output: 2
# print(Solution().networkDelayTime(times, n, k))
# #
# #
# times = [[1,2,1]]
# n = 2
# k = 1
# # Output: 1
# print(Solution().networkDelayTime(times, n, k))
#
# times = [[1,2,1]]
# n = 2
# k = 2
# # Output: -1
# print(Solution().networkDelayTime(times, n, k))
#
# times =[[2,1,1],[2,3,1],[3,4,1]]
# n=4
# k=1
# print(Solution().networkDelayTime(times, n, k))


# accepted solution, somehow
# class Solution(object):
#     def networkDelayTime(self, times, N, K):
#         from collections import defaultdict
#         nodes = defaultdict(dict)
#         Q = set(range(N))
#         for u, v, w in times:
#             nodes[u - 1][v - 1] = w
#         dist = [float('inf')] * N
#         dist[K - 1] = 0
#         while len(Q):
#             u = None
#             for node in Q:
#                 if u == None or dist[node] < dist[u]:
#                     u = node
#             Q.remove(u)
#             for v in nodes[u]:
#                 alt = dist[u] + nodes[u][v]
#                 if alt < dist[v]:
#                     dist[v] = alt
#         d = max(dist)
#         return -1 if d == float('inf') else d