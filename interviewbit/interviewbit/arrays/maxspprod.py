def nearestGT(A):
    # return indices of nearest greater elements (-1) if not found
    res = []
    stack = []
    for i, x in enumerate(A):
        # No point keeping further and smaller elements
        while stack and stack[-1][1] <= x:
            stack.pop()
        k = stack[-1][0] if stack else -1
        res.append(k)
        stack.append((i, x))
    return res


class CorrectSolution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        # We first first nearest greater element indices
        # when scanning right to left.
        # Then we can evaluate on the fly

        if not A:
            return 0

        MODU = 1000000007

        n = len(A)
        rightmost = [n - 1 - j if j >= 0 else 0 for j in nearestGT(reversed(A))]
        rightmost.reverse()

        leftmost = (max(0, j) for j in nearestGT(A))

        return max(j * k for j, k in zip(leftmost, rightmost)) % MODU


class Solution:

    maxint = 9223372036854775807

    def left(self, A, i):
        if i == 0:
            return 0

        j = i - 1
        for k in range(j, 0, -1):
            if A[k] > A[i]:
                return k
        return 0


    def right(self, A, i):
        if i == len(A) - 1:
            return 0
        j = i + 1
        for k in range(j, len(A)):
            if A[k] > A[i]:
                return k
        return 0

    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        maxProd = 0
        for i in range(len(A)):
            leftSpecial = self.left(A, i)
            rightSpecial = self.right(A, i)
            prod = leftSpecial * rightSpecial
            prod = prod % 1000000007
            # print(i, prod)
            if prod > maxProd:
                maxProd = prod

        return maxProd

