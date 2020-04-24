from bisect import bisect_right, bisect_left
from collections import defaultdict

class Solution(object):

    def path_from_i_to_j(self, i, j, graph, n):
        stack = []
        visited = []
        stack.append((i, 0))
        while stack and len(visited) < n:
            node, distance = stack.pop(0)
            visited.append(node)
            if node == j:
                return distance

            for children in graph[node]:
                if children not in visited:

                    stack.insert(0, (children, distance + 1))
        return -1

    def build_matrix(self, n, graph):
        result = [[-1 if i != j else 1 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                result[i][j] = self.path_from_i_to_j(i, j, graph, n)

        return result


    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """


        quiet_idx = sorted([(q, i) for i, q in enumerate(quiet)], key=lambda k: k[0])
        quiet = [q[0] for q in quiet_idx]
        # print(quiet_idx)
        # print()

        # 2n build graph to know how rich someone is
        graph = defaultdict(list)
        for x, y in richer:
            graph[y].append(x)

        richness = self.build_matrix(len(quiet), graph)
        loudest = max(quiet)

        # 1st find who is quieter
        result = [0 for _ in range(len(quiet))]
        for quieteness, person_i in quiet_idx:
            who_is_quieter_than = bisect_right(quiet, quieteness)
            # print(quieteness, person, quiet_idx[0:who_is_quieter_than])
            current = person_i
            loudest_c = loudest
            for loud, person_j in quiet_idx[0:who_is_quieter_than]:
                if richness[person_i][person_j] >= 0 and loud < loudest_c:
                    current = person_j
                    loudest_c = loud
            result[person_i] = current

        return result




richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
# Output: [5,5,2,5,4,5,6,7]
print(Solution().loudAndRich(richer, quiet))



richer = [[0,1],[1,2]]
quiet = [1,0,2]
# Output: [5,5,2,5,4,5,6,7]
print(Solution().loudAndRich(richer, quiet))