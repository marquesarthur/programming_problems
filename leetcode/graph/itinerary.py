from collections import defaultdict
from itertools import chain



# All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

class Solution(object):


    def build_graph(self, tickets):

        g = defaultdict(list)
        for pair in tickets:

            _from, to = pair[0], pair[1]
            g[_from].append(to)

        return g


    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = self.build_graph(tickets)

        # If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string
        for frm, tos in graph.items():  # get key and value from dictionary #sort the destination
            tos.sort(reverse=True)  # we want small to large order

        result = []
        def dfs(graph, source, result):
            while graph[source]:  # when the destination is not empty
                new_source = graph[
                    source].pop()  # let the destination empty if we choose it to pop (pop() means the right one)
                dfs(graph, new_source, result)
            result.append(source)

        dfs(graph, "JFK", result)
        return result[::-1]





tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(Solution().findItinerary(tickets))

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(Solution().findItinerary(tickets))