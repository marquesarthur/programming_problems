class Solution:

    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        N = len(A)

        if N == 0:
            return 1
        else:
            j = N
            i = 0
            while i < j:
                if A[i] > 0:
                    j -= 1
                    A[i], A[j] = A[j], A[i]
                else:
                    i += 1
            if j == N:
                return 1
            else:
                i = j
                while i < N:
                    posNum = A[i] if A[i] > 0 else -A[i]
                    if j + posNum - 1 < N and A[j + posNum - 1] > 0:
                        A[j + posNum - 1] *= -1
                    i += 1
                i = j

                while i < N:
                    if A[i] > 0:
                        break
                    i += 1

                return i - j + 1


# print(Solution().firstMissingPositive([-1, 2, 12, 3, -3, -6, 4, 2, 9]))
print(Solution().firstMissingPositive([1, 2, -1, 4, 5]))
# print(Solution().firstMissingPositive([6, 1, 3, 5, 2, 4, 9, 8, 15]))
