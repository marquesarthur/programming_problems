class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):

        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)


        x_cuts = list(verticalCuts)
        x_cuts.insert(0, 0)
        x_cuts.append(w)

        y_cuts = list(horizontalCuts)
        y_cuts.insert(0, 0)
        y_cuts.append(h)

        max_x = 0
        for i in range(1, len(x_cuts)):
            section = x_cuts[i] - x_cuts[i - 1]
            max_x = max(max_x, section)

        max_y = 0
        for i in range(1, len(y_cuts)):
            section = y_cuts[i] - y_cuts[i - 1]
            max_y = max(max_y, section)

        area = (max_x * max_y) % (10**9 + 7)
        return area



# h = 5
# w = 4
# horizontalCuts = [1, 2, 4]
# verticalCuts = [1, 3]
# print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))

h = 5
w = 4
horizontalCuts = [3,1]
verticalCuts = [1]
print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))