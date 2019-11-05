class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [float('inf') for j in range(0, amount + 1)]
        dp[0] = 0

        for c in coins:
            for j in range(1, amount + 1):
                if c <= j:
                    dp[j] = min(dp[j], dp[j - c] + 1)

        return -1 if dp[amount] > amount else dp[amount]









# coins = [2,3], amount = 6
# you then got a matrix like this
#          0   1   2   3   4   5   6
# 1 round: 0  max max max max max max
# 2 round: 0  max  1  max  2  max  3
# 3 round: 0  max  1   1   2   2   2








coins = [1, 2, 5]
amount = 11

print(Solution().coinChange(coins, amount))


coins = [2]
amount = 3

print(Solution().coinChange(coins, amount))