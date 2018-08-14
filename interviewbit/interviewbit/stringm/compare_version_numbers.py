class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):

        # I can create two new arrays to replace A and B as the split of dot
        # Convert array to int
        # create two variables i and j
        # if A[i] < or A[j]
        # return
        # else increase i and j
        # largest will be the one who does not reach until n

        A = [int(i) for i in A.split(".")]
        B = [int(i) for i in B.split(".")]

        if len(A) < len(B):
            A += [0] * (len(B) - len(A))
        elif len(A) > len(B):
            B += [0] * (len(A) - len(B))

        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[i]:
                return -1
            elif A[i] > B[i]:
                return 1
            else:
                i += 1
                j += 1

        return 0
