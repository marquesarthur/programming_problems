class Solution:

    def pivotSearch(self, A, begin, end, current, pivot):
        if begin > end:
            return

        mid = int((begin + end) / 2)
        if A[mid] < current:
            # we reached an element that is rotated and we must proceed to the left
            pivot.append(mid)
            if A[mid] <= current:
                self.pivotSearch(A, begin, mid - 1, A[mid], pivot)
        else:
            # the list keeps growing and we continue to the right
            self.pivotSearch(A, mid + 1, end, A[mid], pivot)

    def binSearch(self, A, target, begin, end):
        if begin > end:
            return -1

        mid = int((begin + end) / 2)
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            return self.binSearch(A, target, mid + 1, end)
        else:
            return self.binSearch(A, target, begin, mid -1)

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):

        # 1st bin search pivot
        # 2 call bin search in A[0:pivot] and A[pivot:n]
        current = A[int((0 + len(A) - 1) / 2)]
        pivot = []
        self.pivotSearch(A, 0, len(A) - 1, current, pivot)

        truePivot = len(A)
        if pivot:
            truePivot = pivot[len(pivot) - 1]


        result = -1
        if truePivot < len(A):
            left = A[0: truePivot]
            X = left
            Y = A[truePivot:len(A)]
            left = self.binSearch(X, B, 0, len(X)-1)
            right = self.binSearch(Y, B, 0, len(Y) - 1)

            if right != -1:
                result = max(left, right + truePivot)
            else:
                result = left
        else:
            result = self.binSearch(A, B, 0, len(A) - 1)
        return result




#pivot is 4
# print(Solution().search([1, 2 , 3, 4], 1))

# #pivot is 4
# print(Solution().search([2 , 3, 4, 1], 1))
# #
# pivot is 10
print(Solution().search([ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ], 2))