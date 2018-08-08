class Solution:

    def sumStrings(self, A, B):
        # By deffinition B is always greater or equal to A so we need to updated the size of A
        diff = len(B) - len(A)
        if diff > 0:
            zeros = "".join(["0"] * diff)
            A = zeros + A

        A = A[::-1]
        B = B[::-1]

        n = len(A)
        carry_over = 0
        result = ""
        for i in range(n):
            x = int(A[i])
            y = int(B[i])
            op = (x + y + carry_over) % 10
            carry_over = int((x + y + carry_over) / 10)
            result = str(op) + result

        if carry_over != 0:
            result = str(carry_over) + result

        return result


    def multiplyDigits(self, multiplier, A, zeros):
        result = zeros
        carry_over = 0
        for digit in A:
            x = int(multiplier)
            y = int(digit)
            op = (x * y + carry_over) % 10
            carry_over = int((x * y + carry_over) / 10)

            result = str(op) + result

        if carry_over != 0:
            result = str(carry_over) + result

        return result

    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        summations = []
        if not A and not B:
            return 0

        A = A[::-1]
        B = B[::-1]

        for i, digit in enumerate(B):
            zeros = "".join(["0"] * i)
            summations.append(self.multiplyDigits(digit, A, zeros))

        _sum = "0"
        for value in summations:
            _sum = self.sumStrings(_sum, value)


        while True:
            if _sum[0] == "0" and len(_sum) > 1:
                _sum = _sum[1:len(_sum)]
            else:
                break

        return _sum

# print(Solution().multiply("99999", "99999"))