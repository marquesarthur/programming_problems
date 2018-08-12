# (A O(n) method: use Dequeue)
# We create a Dequeue, Qi of capacity k, that stores only useful elements of current window of k elements.
# An element is useful if it is in current window and is greater than all other
# elements on left side of it in current window.
# We process all array elements one by one and maintain Qi to contain useful elements
# of current window and these useful elements are maintained in sorted order.
# The element at front of the Qi is the largest and element at rear of Qi is the
# smallest of current window.

class Solution:


    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        # what if B <= 0
        # what if not A

        if B > len(A):
            return [max(A)]

        queue = []
        for i in range(0, min(B, len(A))):

            while queue and A[queue[-1]] < A[i]:
                queue.pop()

            queue.append(i)

        # starts with max value
        result = [A[queue[0]]]

        # [1 3 -1 -3 5 3 6 7]
        #  0 1  2  3 4 5 6 7


        for i in range(B, len(A)):

            min_i = i + 1 - B
            while queue and queue[0] < min_i:
                queue = queue[1: len(queue)]

            while queue and A[queue[-1]] < A[i]:
                queue.pop()

            queue.append(i)

            result.append(A[queue[0]])

        return result


# A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# B = 2
A = [648, 614, 490, 138, 657, 544, 745, 582, 738, 229, 775, 665, 876, 448, 4, 81, 807, 578, 712, 951, 867, 328, 308,
     440, 542, 178, 637, 446, 882, 760, 354, 523, 935, 277, 158, 698, 536, 165, 892, 327, 574, 516, 36, 705, 900, 482,
     558, 937, 207, 368]
B = 9
#
C = "745 745 775 775 876 876 876 876 876 876 876 951 951 951 951 951 951 951 951 951 882 882 882 882 935 935 935 935 935 935 935 935 935 892 892 892 900 900 900 937 937 937"
C = [int(i) for i in C.split()]

# A = [1]
# B = 1
result = Solution().slidingMaximum(A, B)
print(result)
print(result == C)
