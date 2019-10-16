"""
Given n ropes of different lengths, we need to connect these ropes into one rope.
We can connect only 2 ropes at a time.
The cost required to connect 2 ropes is equal to sum of their lengths.
The length of this connected rope is also equal to the sum of their lengths.
This process is repeated until n ropes are connected into a single rope.
Find the min possible cost required to connect all ropes.
"""

from bisect import bisect_right


class Solution():
    """
        A typical priority queue problem, every step you pick two shortest ropes and connect them,
        then put it back to the selections, you keep this process until there is only one left.
    """

    def minCost(self, ropes):

        ropes = sorted(ropes)

        total_cost = 0
        while ropes:
            a, b = 0, 0
            if ropes:
                x = ropes.pop(0)
                if x:
                    a = x

            if ropes:
                x = ropes.pop(0)
                if x:
                    b = x

            costs = a + b

            if ropes:
                idx = bisect_right(ropes, costs)
                ropes.insert(idx, costs)
            total_cost += costs

        return total_cost


ropes = [8, 4, 6, 12]  # 58
print(Solution().minCost(ropes))
#
ropes = [20, 4, 8, 2]  # 54
print(Solution().minCost(ropes))
#
ropes = [1, 2, 5, 10, 35, 89]  # 224
print(Solution().minCost(ropes))
#
# ropes = [2, 2, 3, 3]  # 20
# print(Solution().minCost(ropes))
