class Solution(object):
    """
        THIS SOLUTION IS NOT CORRECT
        So the problem is essentially 2 separate cases.

        But it's important to keep in mind that the L+M maximum could be reached before L & M separate from each other
        So you cannot divide each case into simply 2 steps:

        find the global maximum of the window on the left
        find the maximum of the second window in the region to the right of the first window
        case 1: L-window comes before M-windows
        Once L-window reaches it's global maximum, it will stop sliding but M window can keep going on

        case 2: M-window comes before L-windows
        Once M-window reaches it's global maximum, it will stop sliding but L window can keep going on

        CHECK: https://www.geeksforgeeks.org/maximum-sum-two-non-overlapping-subarrays-of-given-size/
    """




    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        for i in range(1, len(A)):
            A[i] += A[i - 1]

        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        # window  | --- L --- | --- M --- |
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M])

        # window  | --- M --- | --- L --- |
        for i in range(L + M, len(A)):
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Mmax + A[i] - A[i - L])


        return res


#
A = [0, 1, 5, 5, 1, 2, 3]
L = 3
M = 2

print(Solution().maxSumTwoNoOverlap(A, L, M)) # 8

#
# A = [0,6,5,2,2,5,1,9,4]
# L = 1
# M = 2
# print(Solution().maxSumTwoNoOverlap(A, L, M)) # 20


#
# A = [3,8,1,3,2,1,8,9,0]
# L = 3
# M = 2
# print(Solution().maxSumTwoNoOverlap(A, L, M)) # 29
#
#
#
# A = [2,1,5,6,0,9,5,0,3,8]
# L = 4
# M = 3
# print(Solution().maxSumTwoNoOverlap(A, L, M)) # 31

