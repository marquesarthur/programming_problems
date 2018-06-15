import operator
import sys

right = (0, 1)
bottom = (1, 0)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        sys.setrecursionlimit(5000)
        endPoint = (A - 1, B -1)
        currentPoint = (0, 0)

        # print currentPoint

        nextRight = tuple(map(operator.add, currentPoint, right))
        nextBottom = tuple(map(operator.add, currentPoint, bottom))

        # move right and also to bottom
        paths = self.walkToEndPoint(nextBottom, endPoint) + self.walkToEndPoint(nextRight, endPoint)

        return uniquePaths

    def walkToEndPoint(self, currentPoint, endPoint):
        # print currentPoint
        if currentPoint == endPoint:
            return 1
        elif currentPoint[0] > endPoint[0]:
            return 0
        elif currentPoint[1] > endPoint[1]:
            return 0
        else:
            nextRight = tuple(map(operator.add, currentPoint, right))
            nextBottom = tuple(map(operator.add, currentPoint, bottom))
            return self.walkToEndPoint(nextBottom, endPoint) + self.walkToEndPoint(nextRight, endPoint)


assert(Solution().uniquePaths(1, 3000) == 1)
assert(Solution().uniquePaths(3000, 1) == 1)
assert(Solution().uniquePaths(2, 2) == 2)
assert(Solution().uniquePaths(3, 7) == 28)
assert(Solution().uniquePaths(15, 12) == 4457400)