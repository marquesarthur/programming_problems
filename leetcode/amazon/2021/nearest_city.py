import sys
from math import sqrt
from collections import defaultdict


class Point(object):

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.id == other.id
        return False

    def distance(self, p2):
        return sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)  # Pythagorean theorem


def nearest_city(n, points, x, y, q, queries):
    points_in_same_coordinates = defaultdict(list)
    id_to_point = dict()

    for __p, __x, __y in zip(points, x, y):
        p = Point(__p, __x, __y)

        points_in_same_coordinates[__x].append(p)
        points_in_same_coordinates[__y].append(p)
        id_to_point[__p] = p

    results = []
    for query in queries:

        r = None
        p = id_to_point[query]

        in_same_coordinates = points_in_same_coordinates[p.x] + points_in_same_coordinates[p.y]
        in_same_coordinates = list(filter(lambda k: k.id != p.id, in_same_coordinates))

        if in_same_coordinates:
            min_dist = sys.maxsize
            for other in in_same_coordinates:
                dist = p.distance(other)
                if dist < min_dist:
                    min_dist = dist
                    r = other

        if r:
            results.append(r.id)
        else:
            results.append(r)

    return results


numOfPoints = 3
points = ["p1", "p2", "p3"]
xCoordinates = [30, 20, 10]
yCoordinates = [30, 20, 30]
numOfQueriedPoints = 3
queriedPoints = ["p3", "p2", "p1"]

print('')
print('Output: ["p1", NONE, "p3"]')
print(nearest_city(numOfPoints, points, xCoordinates, yCoordinates, numOfQueriedPoints, queriedPoints))

numOfPoints = 5
points = ["p1", "p2", "p3", "p4", "p5"]
xCoordinates = [10, 20, 30, 40, 50]
yCoordinates = [10, 20, 30, 40, 50]
numOfQueriedPoints = 5
queriedPoints = ["p1", "p2", "p3", "p4", "p5"]

print('')
print('Output: [NONE, NONE, NONE, NONE, NONE]')
print(nearest_city(numOfPoints, points, xCoordinates, yCoordinates, numOfQueriedPoints, queriedPoints))
