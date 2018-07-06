class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        out = []
        carry_over = False
        for i, val in enumerate(reversed(A)):
            if i == 0:
                carry_over = ((val + 1) % 10 == 0)
                new = (val + 1) % 10
            elif carry_over:
                carry_over = ((val + 1) % 10 == 0)
                new = (val + 1) % 10
            else:
                carry_over = False
                new = val
            out.append(new)
        if carry_over:
            out.append(1)
        out = list(reversed(out))

        while len(out) > 0 and out[0] == 0:
            out.pop(0)


        return out


