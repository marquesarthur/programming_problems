
class Solution:
    rules = {
        0: [1, 2],
        1: [2],
        2: [0, 1, 3, 4],
        3: [0, 4],
        4: [3, 1],
    }

    def solve(self, A):
        init = ["a", "e", "i", "o", "u"]
        matrix = [None] * 2
        matrix[0] = [1, 1, 1, 1, 1]
        matrix[1] = [2, 1, 4, 2, 2]



        if A == 1:
            return sum(matrix[0])

        if A == 2:
            return sum(matrix[1])

        result = 0
        last_row = matrix[1]
        constant = (1e9 + 7)
        for i in range(3, A + 1):
            current_row = [0] * len(init)
            for j, value in enumerate(current_row):
                for r in self.rules[j]:
                    current_row[j] += (last_row[r] % constant)




            result = sum(current_row)
            last_row = current_row

        return int(result % constant)









class MatrixSolution:

    seen = {}

    rules = {
        "a": ["e", "i"],
        "e": ["i"],
        "i": ["a", "e", "o", "u"],
        "o": ["a", "u"],
        "u": ["o", "e"],
    }

    def getStrCount(self, currentStr, A, result):
        if len(currentStr) == A:
            if currentStr not in result:
                result.append(currentStr)
                return 1

        currentC =  currentStr[len(currentStr) - 1]
        nextC = self.rules[currentC]

        sum = 0
        for c in nextC:
            nextStr = currentStr + c
            sum += self.getStrCount(nextStr, A, result)

        return sum

    # @param A : integer
    # @return an integer
    def solve(self, A):
        # base case = 1

        init = ["a", "e", "i", "o", "u"]

        self.seen[0] = (len(init), init)

        # result = []
        # for c in init:
        #     self.seen[1] = self.getStrCount(c, 1, result), result

        for i in range(1, A):
            previous_count, previous_strs = self.seen[i - 1]
            result = []
            sum = 0
            for currentStr in previous_strs:
                currentC = currentStr[len(currentStr) - 1]
                nextCs = self.rules[currentC]
                for c in nextCs:
                    result.append(currentStr + c)
                    sum += 1

            self.seen[i] = (sum, result)
            self.seen.pop(i - 2, None)

        count, k = self.seen[A - 1]
        constant = (1e9 + 7)
        return int(count % constant)


