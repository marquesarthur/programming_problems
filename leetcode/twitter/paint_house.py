class Solution(object):

    def paint(self, prices, last_color):
        color_map = {
            0: (1, 2),
            1: (0, 2),
            2: (0, 1)
        }

        total_price = 0

        for i in xrange(len(prices)):
            next_i, next_j = color_map[last_color]

            if prices[i][next_i] < prices[i][next_j]:
                total_price += prices[i][next_i]
                last_color = next_i
            else:
                total_price += prices[i][next_j]
                last_color = next_j

        return total_price

    def paintHouse(self, prices):

        a = self.paint(prices, 0)
        b = self.paint(prices, 1)
        c = self.paint(prices, 2)

        return min(a, b, c)


input = [
    [17, 2, 1], [16, 16, 1], [14, 3, 19], [3, 1, 8]
]
print(Solution().paintHouse(input))
