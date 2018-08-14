class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):

        # This is based on Majority Element algorithm

        first = max(A) + 2  # will guarantee that I have an element outside the array
        second = max(A) + 2  # will guarantee that I have an element outside the array
        count_1st = 0
        count_2nd = 0
        n = len(A)

        for value in A:
            if value == first:
                count_1st += 1
            elif value == second:
                count_2nd += 1
            elif count_1st == 0:
                count_1st += 1
                first = value
            elif count_2nd == 0:
                count_2nd += 1
                second = value
            else:
                count_1st -= 1
                count_2nd -= 1

        # At this point first and second will have the elements that occurred the most in the array
        count_1st = 0
        count_2nd = 0
        for value in A:
            if value == first:
                count_1st += 1
            elif value == second:
                count_2nd += 1

            if count_1st > n / 3:
                return first
            elif count_2nd > n / 3:
                return second

        return -1
