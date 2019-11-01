def knapsack(n, values, weights, W):
    K = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(
                    values[i - 1] + K[i - 1][w - weights[i - 1]],
                    K[i - 1][w],
                )
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


def maximumTotalWeight(weights, tasks, p):
    # Write your code here
    tasks = [2 * i for i in tasks]
    return knapsack(len(tasks), weights, tasks, p)


tasks = [2, 2, 3, 4]
weights = [2, 4, 4, 5]
p = 15

print(maximumTotalWeight(weights, tasks, p))