import sys


class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        if not A:
            return A

        if len(A) == 1:
            return A

        # iterate from n to 0
        # find 1st element that is not in increasing order, e.g.
        #   1, 2, 3 -- 2 is not in increasing order
        #   1, 3, 2 -- 1 is not in increasing order
        i = len(A) - 1
        while i > 0 and A[i - 1] > A[i]:
            i -= 1

        if i == 0:
            return sorted(A)

        i -= 1  # move pointer to that element

        # iterate from n to 0
        # find 1st element greater than A[i], e.g.
        #   for A[1] = 2, A[2] = 3 is greater
        #   for A[0] = 1, A[2] = 2 is greater
        j = len(A) - 1
        while j > i:
            if A[j] > A[i]:
                break
            j -= 1

        # swap elements in previous step
        A[i], A[j] = A[j], A[i]

        # sort everything to the right of the swapped element
        A[i + 1:] = sorted(A[i + 1:])

        return A


s = Solution()

print(s.nextPermutation([1, 2, 3]) == [1, 3, 2])
print(s.nextPermutation([1, 3, 2]) == [2, 1, 3])
print(s.nextPermutation([2, 1, 3]) == [2, 3, 1])
print(s.nextPermutation([2, 3, 1]) == [3, 1, 2])
print(s.nextPermutation([3, 1, 2]) == [3, 2, 1])
print(s.nextPermutation([3, 2, 1]) == [1, 2, 3])
