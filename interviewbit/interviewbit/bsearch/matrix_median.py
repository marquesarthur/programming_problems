from bisect import bisect_right as upper_bound


# First we find the minimum and maximum elements in the matrix.
# Minimum element can be easily found by comparing the first element of each row,
# and similarly the maximum element can be found by comparing the last element of each row.

# Then we use binary search on our range of numbers from minimum to maximum,
# we find the mid of the min and max, and get count of numbers less than our mid.
# And accordingly change the min or max.

# For a number to be median, there should be (r*c)/2 numbers smaller than that number.
# So for every number, we get the count of numbers less than that by using upper_bound()
# in each row of matrix, if it is less than the required count,
# the median must be greater than the selected number,
# else the median must be less than or equal to the selected number.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        r = len(A)
        c = len(A[0])
        mi = A[0][0]
        mx = 0
        for i in range(r):
            if A[i][0] < mi:
                mi = A[i][0]
            if A[i][c - 1] > mx:
                mx = A[i][c - 1]

        desired = (r * c + 1) / 2

        while (mi < mx):
            mid = mi + (mx - mi) / 2
            place = 0

            # Find count of elements smaller than mid
            for i in range(r):
                j = upper_bound(A[i], mid)
                place = place + j
            if place < desired:
                mi = mid + 1
            else:
                mx = mid

        return mi
