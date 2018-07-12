class Solution:
    def generate_new_row(self, last_row):
        result = [1]
        for c in range(len(last_row) - 1):
            x = last_row[c] + last_row[c + 1]
            result.append(x)
        result.append(1)
        return result

    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        first_row = [1]
        second_row = [1, 1]

        if A <= 0:
            return []
        elif A == 1:
            return [first_row]
        elif A == 2:
            return [first_row, second_row]
        else:
            triangle = [first_row, second_row]
            for i in range(2, A):
                last_row = triangle[i - 1]
                new_row = self.generate_new_row(last_row)
                triangle.append(new_row)

            return triangle
