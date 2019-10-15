class Solution():

    def minDiscout(self, prices):

        stack = []
        ans = [-1 for _ in prices]

        for i in xrange(len(prices) - 1, -1, -1):
            current = prices[i]
            if stack:
                next = prices[stack[-1]]

                while stack and current < next:
                    stack.pop()
                    if stack:
                        next = prices[stack[-1]]

            if stack:
                ans[i] = stack[-1]

            stack.append(i)

        total = 0
        missing_indexes = []
        for i, idx in enumerate(ans):
            if idx == -1:
                missing_indexes.append(i)
                total += prices[i]
            else:
                total += prices[i] - prices[idx]

        return total




# solution 1: for each i for up to i:len(A)
# worst case array sorted in increasing order

A = [5, 4, 5, 1, 3, 3, 8, 2]
print(Solution().minDiscout(A))