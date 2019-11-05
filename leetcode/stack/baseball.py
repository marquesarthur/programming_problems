class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        data = []
        for i in ops:
            if i not in ["C", "D", "+"]:
                data.append(int(i))
            elif i == "C":
                data.pop()
            elif i == "D":
                data.append(2 * data[-1])
            elif i == "+":
                data.append(data[-1] + data[-2])


        _sum = sum(data)
        return _sum







input = ["5","2","C","D","+"]
# print(Solution().calPoints(input))


input = ["5","-2","4","C","D","9","+","+"]
print(Solution().calPoints(input))