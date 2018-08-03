class Solution:
    def threeSum(self, A):

        A = sorted(A)
        n = len(A)

        result = set()

        for i in range(n):

            j = i + 1
            k = n - 1

            target = A[i]

            while j < k:
                if target + A[j] + A[k] < 0:
                    j += 1
                elif target + A[j] + A[k] > 0:
                    k -= 1
                else:
                    result.add((A[i], A[j], A[k]))
                    j += 1

        return sorted(list(result))


# Exceeds time limit but does the job
class MatrixSolution:
    def binarySearch(self, A, x):
        begin = 0
        end = len(A) - 1

        while begin <= end:
            mid = int(begin + (end - begin) / 2)

            if A[mid] == x:
                return mid
            elif A[mid] > x:
                end = mid - 1
            else:
                begin = mid + 1

        return -1

    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):

        A = sorted(A)
        S = list(A)
        n = len(A)
        B = [None] * len(A)

        for i in range(len(A)):
            B[i] = [None] * n
            for j in range(i + 1, len(A)):
                k = A[i] + A[j]
                B[i][j] = -k

        result = []
        for i in range(n):
            for j in range(i + 1, n):

                x = B[i][j]
                s_aux = [x for a, x in enumerate(A) if a != i and a != j and A[a] is not None]
                k = self.binarySearch(s_aux, x)
                if k != -1 and A[i] is not None and A[j] is not None:
                    k = self.binarySearch(S, x)
                    aux = sorted([A[i], A[j], S[k]])

                    exists = False
                    for r in result:
                        if r[0] == aux[0] and r[1] == aux[1] and r[2] == aux[2]:
                            exists = True
                            break

                    if not exists:
                        result.append(aux)

        ret = [(r[0], r[1], r[2]) for r in result]
        return ret
