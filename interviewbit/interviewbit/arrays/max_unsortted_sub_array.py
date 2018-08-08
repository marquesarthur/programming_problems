class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        if not A:
            return [-1]

        if len(A) == 1:
            return [-1]

        _sorted = True
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                _sorted = False
                break

        if _sorted:
            return [-1]

        n = len(A) - 1
        start = 0
        while start < n - 1:
            if A[start] > A[start + 1]:
                break
            start += 1

        end = n
        while end > 0:
            if A[end] < A[end - 1]:
                break
            end -= 1

        Aux = A[start: end + 1]
        # print(Aux, start, end)
        max_aux = max(Aux)
        min_aux = min(Aux)

        if A[0:start]:
            g = 0
            while g < start:
                if A[g] > min_aux:
                    start = g
                    break
                g += 1

        if end < len(A):
            i = len(A) - 1
            while i > end:
                if A[i] < max_aux:
                    end = i
                    break
                i -= 1

        return [start, end]


# Solution().subUnsort([1, 3, 2, 4, 2, 3])
# print(Solution().subUnsort([ 1, 1, 4, 6, 8, 8, 13, 13, 13, 14, 17, 18, 14 ]))
print(Solution().subUnsort([1, 2, 3, 4, 5]))
