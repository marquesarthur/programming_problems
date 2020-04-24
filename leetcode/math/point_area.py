from collections import defaultdict
import sys


class Solution:
    def minAreaRect(self, points):

        # for a rectangle, there must be two points in the same X and different Y
        #   eg: [1,1] and [1, 3]
        # and two points with different X and same Y
        #   e.g. [3, 1] and [1, 1]

        # pass through array, build key X to points
        # build key Y to points
        # filter keys with count > 2
        # compute min area if it meats conditions

        # first sort points O(n log n)

        if len(points) <= 3:
            return 0

        points = sorted(points, key=lambda k: (k[0], k[1]))

        Ys = defaultdict(list)

        for p in points:
            Ys[p[1]].append(p)

        # first sort points O(n log n)

        points = sorted(points, key=lambda k: (k[0], k[1]))

        result = sys.maxsize
        for i in range(1, len(points)):
            P1 = points[i - 1]
            P2 = points[i]

            if P1[0] == P2[0]:  # two points at same X and different Y
                y1 = P1[1]
                y2 = P2[1]

                # right now I have p1 and p2, I need p3 in y1 and p4 in y2
                P3_lst = list(filter(lambda k: k[0] > P1[0] and k[1] == y1, Ys[y1]))
                Xs_in_P3 = [k[0] for k in P3_lst]


                P4_lst = list(filter(lambda k: k[0] > P2[0] and k[1] == y2, Ys[y2]))
                Xs_in_P4 = [k[0] for k in P4_lst]

                final = set(Xs_in_P3).intersection(Xs_in_P4)
                P3_lst = list(filter(lambda k: k[0] in final,  P3_lst))
                P4_lst = list(filter(lambda k: k[0] in final, P4_lst))

                if P3_lst and P4_lst:
                    height = y2 - y1
                    width = P3_lst[0][0] - P1[0]
                    if height > 0 and width > 0:
                        result = min(result, height * width)

        return result








points = [[0,1],[1,3],[3,3],[4,4],[1,4],[2,3],[1,0],[3,4]]

print(Solution().minAreaRect(points))

