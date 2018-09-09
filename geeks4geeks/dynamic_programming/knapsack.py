class KnapscackDynamicProgramming(object):
    def solve(self, n, values, weights, W):
        K = [[0 for x in range(W + 1)] for y in range(n + 1)]

        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif weights[i - 1] <= w:
                    K[i][w] = max(
                        values[i - 1] + K[i-1][w - weights[i - 1]],
                        K[i-1][w],
                    )
                else:
                    K[i][w] = K[i-1][w]

        return K[n][W]


class KnapscackNaive(object):

    def solve(self, i, values, weights, W):
        if i == -1 or W == 0:
            return 0

        if weights[i] > W:
            return self.solve(i - 1, values, weights, W)

        else:
            return max(
                values[i] + self.solve(i - 1, values, weights, W - weights[i]),
                self.solve(i - 1, values, weights, W)
            )


class KnapscackBruteForce(object):
    def __init__(self):
        pass

    def find_solutions(self, i, values, weights, result, W):
        if i < len(values) and i < len(weights):

            new_solutions = []
            for j in result:
                w = sum([weights[k] for k in j])
                if weights[i] + w <= W:
                    new_solutions.append(list(j) + [i])

            if new_solutions:
                result += new_solutions
            if weights[i] <= W:
                result.append([i])

            self.find_solutions(i + 1, values, weights, result, W)

    def solve(self, values, weights, W):
        if not values or not weights:
            return 0

        result = []
        i = 0
        self.find_solutions(i, values, weights, result, W)

        _max = 0
        _best = None
        for solution in result:
            value_current_solution = sum(values[k] for k in solution)
            if value_current_solution > _max:
                _best = solution
                _max = value_current_solution

        return _best


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
print(KnapscackDynamicProgramming().solve(len(values), values, weights, W))
