class Solution:
    # 1211
    def nextFrom(self, current):
        i = 0
        result = []
        while i < len(current):  # i = 2
            count = 1
            j = i + 1  # j = 3
            while j < len(current) and current[i] == current[j]:
                j += 1  # j = 4
                count += 1
            result.append(str(count) + current[i])
            i = j

        return "".join(result)

    # @param A : integer
    # @return a strings
    def countAndSay(self, A):

        current = "1"

        for i in range(1, A):
            current = self.nextFrom(current)

        return current
