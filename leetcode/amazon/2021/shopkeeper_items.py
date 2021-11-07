def find_discount_prices(val):
    stack = []
    res = [0 for _ in range(len(val))]
    for i in range(len(val) - 1, -1, -1):

        current = val[i]
        while stack and stack[-1] > current:
            stack.pop()  # means there is no value greater than current value

        res[i] = -1 if not stack else stack[-1]
        stack.append(current)

    profit = 0
    result = []

    for i in range(len(val)):
        discount = 0
        if res[i] == -1:
            result.append(i)
        else:
            discount = res[i]

        profit += val[i] - discount

    return profit, result


val = [2, 3, 1, 2, 4, 2]
print(find_discount_prices(val))
# 18
# 2 5


val = [5, 1, 3, 4, 6, 2]
print(find_discount_prices(val))
# 14
# 1 5

val = [1, 3, 3, 2, 5]
print(find_discount_prices(val))
# 9
# 0 3 4
