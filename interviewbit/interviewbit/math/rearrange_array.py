class IntegerSolution:
    def interweave(self, x, y, n):
        return x + (y * n)

    def unweave(self, x, n):
        return int(x / n)

    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        n = len(A)
        for i in range(n):
            A[i] = self.interweave(A[i], A[A[i]] % n, n)

        for i in range(len(A)):
            A[i] = self.unweave(A[i], n)

        return A


class StringSolution:
    def interweave(self, x, y):
        a = str(x)
        b = str(y)
        if len(a) > len(b):
            diff = len(b) - len(a)
            aux = "0" * diff
            b = aux + b
        elif len(b) < len(a):
            diff = len(a) - len(b)
            aux = "0" * diff
            a = aux + a

        zipped = zip(a, b)
        return "".join([k[0] for k in zip(*zipped)])

    def unweave(self, x):
        num = ""
        for i in range(1, len(x), 2):
            num += x[i]

        return int(num)

    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):

        for i in range(len(A)):
            A[i] = self.interweave(A[i], A[A[i]])

        for i in range(len(A)):
            A[i] = self.unweave(A[i])

        return A
