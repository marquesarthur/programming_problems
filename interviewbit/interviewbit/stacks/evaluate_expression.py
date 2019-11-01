class Solution:
    def do_operation(self, a, b, operator):

        if b == 0 and operator == "/":
            a, b = b, a
        if a == 0 and b == 0 and operator == "/":
            return 0

        result = {
            "+": (a + b),
            "-": (a - b),
            "*": (a * b),
            "/": (a / b) if b != 0 else 0
        }
        return result[operator]

    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):

        stack = []
        math_operators = ["+", "-", "/", "*"]

        for i in A:
            if i in math_operators:
                # do computation
                b = stack.pop()
                a = stack.pop()
                c = self.do_operation(a, b, i)
                stack.append(c)
            else:
                stack.append(int(i))

        return stack.pop()


A = ["-2", "-1", "2", "+", "-1", "-", "-", "2", "-2", "1", "-", "+", "-", "-2", "-2", "-", "-1", "2", "-2", "-", "-2",
     "-1", "+", "1", "1", "-", "-1", "+", "1", "*", "*", "2", "+", "*", "-", "-2", "1", "-2", "*", "+", "-2", "*", "1",
     "*", "-", "*", "*"]

result = Solution().evalRPN(A)
print(result)
#
# A = ["-1", "-1", "1", "-2", "+", "*", "+", "-1", "2", "+", "-2", "-1", "*", "-1", "1", "-", "2", "-", "-1", "*", "-1",
#      "1", "-2", "1", "1", "-2", "2", "2", "*", "*", "2", "+", "-2", "-2", "-", "*", "+", "1", "-", "1", "1", "-", "-2",
#      "-1", "*", "*", "-", "*", "-", "*", "-", "-", "+", "-", "-"]
# result = Solution().evalRPN(A)
# print(result) # 4