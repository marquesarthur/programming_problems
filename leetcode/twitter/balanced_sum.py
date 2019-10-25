class Solution():

    def balancedSum(self, sales):
        # Write your code here
        total = sum(sales[2:])
        left_sum, right_sum = sales[0], total
        for i in xrange(1, len(sales) - 1):
            if left_sum == right_sum:
                return i
            right_sum -= sales[i + 1]
            left_sum += sales[i]




        return -1



sales = [1, 2, 3, 3]
print(Solution().balancedSum(sales)) # 2
#
sales = [1, 2, 3, 4, 6]
print(Solution().balancedSum(sales)) # 3


sales = [1, 2, 1]
print(Solution().balancedSum(sales)) # 1

