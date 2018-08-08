class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        _max = 0
        largest = 0

        for i in range(len(A)):
            if A[i] > largest:
                largest = A[i]

            _max += A[i]

        window = 0
        if largest > B:
            window = 1
        else:
            window = 2

        # This means that the sum of all elements is smaller than target
        if _max < B:
            return - 1

        count = 0
        current = 0
        while window < len(A) + 1:


            _sum = A[current]

            j = 1
            _next = current
            while j < window and _sum < B and _next + 1 < len(A):
                _next += 1
                j += 1
                _sum += A[_next]


            if _sum >= B:
                count += 1
            current += 1

            if current == len(A):
                current = 0
                window += 1
                if count > 0:
                    break

        if count > 0:
            return count
        return -1


A = [ 1, 2, 3, 4, 5 ]
B = 7


print(Solution().solve(A, B))
