from itertools import combinations

class Solution:
    def twoCitySchedCost(self, costs):

        result = sum([max(x[0], x[1]) for x in costs])
        for c in combinations([idx for idx, _ in enumerate(costs)], int(len(costs) / 2)):
            A = set(c)
            sum_A, sum_B = 0, 0
            for idx, _ in enumerate(costs):
                if idx in A:
                    sum_A += costs[idx][0]
                else:
                    sum_B += costs[idx][1]
            total = sum_A + sum_B
            result = min(total, result)

        return result


from itertools import combinations


class SolutionOptimal:
    def twoCitySchedCost(self, costs) -> int:
        placeA = []
        placeB = []
        s = 0
        for cost in costs:
            if cost[-1] > cost[0]:
                s += cost[0]
                placeA.append(cost[-1] - cost[0])
            else:
                s += cost[-1]
                placeB.append(cost[0] - cost[-1])
        if len(placeA) == len(placeB):
            return s
        else:
            if len(placeA) > len(placeB):
                long = placeA
            else:
                long = placeB
            long.sort()
            while len(long) > len(costs) / 2:
                s += long[0]
                del long[0]
            return s