class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        a = str(A)
        i = 0
        j = len(a) - 1

        while i < j:
            if a[i] is not a[j]:
                return False
            i += 1
            j -= 1

        return True
