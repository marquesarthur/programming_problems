class Solution:
    def nearestGT(self, A, B, C):
        # stack = []
        begin = 0
        end = len(A)
        nearest = -1
        while begin < end:
            mid = int((begin + end) / 2)
            x = A[mid]
            if x < C and len(str(x)) <= B:
                # stack.append((x, mid))
                begin = mid + 1
                nearest = begin
            elif x > C and len(str(x)) <= B:
                # stack.append((x, mid))
                end = mid - 1
                nearest = end
            else:
                nearest = mid
                break

        if begin == end:
            return len(A)

        for i in range(nearest, 0, -1):
            if A[i] <= C and len(str(A[i])) <= B:
                return i + 1

        return 0


    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if not A:
            return 0
        return self.nearestGT(A, B, C)
