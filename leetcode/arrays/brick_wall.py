from collections import defaultdict
import sys


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        brick_wall = defaultdict(list)

        _min = 0
        _max = sys.maxint
        if wall and wall[0]:
            _max = sum(wall[0])

        _best_line = -sys.maxint - 1

        for row in wall:
            total = 0
            for idx, brick in enumerate(row):

                total += brick
                if _min < total < _max:
                    brick_wall[total].append(idx)


        if brick_wall.keys():
            aux = sorted([(k, len(v)) for k, v in brick_wall.items()], key=lambda a: a[1], reverse=True)
            _best_line = aux.pop(0)[0]

        result = 0
        for row in wall:
            total = 0
            for idx, brick in enumerate(row):

                total += brick

                if total == _best_line:
                    break
                elif total > _best_line:
                    result += 1
                    break

        return result


input = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]
]

print(Solution().leastBricks(input))

input = [
    [1, 1],
    [2],
    [1, 1]
]
print(Solution().leastBricks(input))

# # convert brick length into location of cracks
# for row in wall:
#     # exclude the beginning and the end of the wall (they aren't cracks)
#     for i in range(1, len(row) - 1):
#         row[i] += row[i - 1]
#     # remove last element of the wall
#     row.pop()
#
# # count the frequency of each crack
# cracks = collections.Counter()
# for row in wall:
#     cracks.update(row)
# if cracks:
#     most_cracks = cracks[max(cracks, key=cracks.get)]
# else:
#     most_cracks = 0
# cut_bricks = len(wall) - most_cracks
# return cut_bricks