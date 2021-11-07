CASH_LIMIT = 1000
TIME_LIMIT = 60
name = 0
time = 1
amount = 2
city = 3


class Solution(object):

    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """

        transactions = sorted(transactions, key=lambda k: (k.split(",")[0], int(k.split(",")[1])))

        invalid = set()
        for i in range(len(transactions)):

            current = transactions[i].split(",")
            current[amount] = int(current[amount])
            current[time] = int(current[time])

            if current[amount] > CASH_LIMIT:
                invalid.add(i)
            if i > 0:
                previous = transactions[i - 1].split(",")
                previous[amount] = int(previous[amount])
                previous[time] = int(previous[time])

                if current[name] == previous[name] and (current[time] - previous[time] <= TIME_LIMIT) and current[
                    city] != previous[city]:
                    invalid.add(i - 1)
                    invalid.add(i)

        return [transactions[i] for i in invalid]


t = ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
print(Solution().invalidTransactions(t))
