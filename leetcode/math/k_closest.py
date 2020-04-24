import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt( (self.x - p.x)**2 + (self.y - p.y)**2)


from collections import defaultdict

class Solution:

    def k_closes(self, points, point, k):
        distances = defaultdict(list)

        point = Point(point[0], point[1])

        for p in points:
            current = Point(p[0], p[1])
            dist = current.distance(point)

            distances[dist].append(current)

        result = []

        for d in sorted(distances.keys()):
            to_add = distances[d]
            for a in to_add:
                if len(result) < k:
                    result.append(a)
                else:
                    return [(p.x, p.y) for p in result]

        return result


points = [[3, 3], [5, -12], [-2, 4], [0, 5], [9, 4], [-22, 6]]
p = [1, -2]
k = 4
print(Solution().k_closes(points, p, k))




