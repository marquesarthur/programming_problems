class BestSolution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        rev = A[::-1]
        l = len(A)
        while l > 0:
            for i in range(0, len(A) - l + 1):
                half = int(l / 2)
                left = A[i : i + half]
                right = rev[len(A) - (i + l) : len(A) - (i + l - half)]
                if left == right:
                    result =  A[i:i+l]
                    return result
            l -= 1
        return None

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):

        n = len(A)

        # length, begin, end
        k = [[(0, "") for i in range(n+1)] for j in range(n + 1)]

        i = 0
        while i < n+1:
            j = 0

            while j < n+1:
                if i == 0 or j == 0:
                    k[i][j] = (0, "")
                else:

                    B = A[i-1:j]
                    if B == B[::-1]:
                        last = k[i - 1][j]
                        k[i][j] = (len(B), B) if len(B) > last[0] else last
                    else:
                        k[i][j] = k[i - 1][j] if k[i - 1][j][0] > k[i][j-1][0] else k[i][j-1]

                j += 1

            i += 1

        result = k[n][n]
        return result[1]


# BestSolution().longestPalindrome("aaaabaaa")


BestSolution().longestPalindrome("abbcccbbbcaaccbababcbcabca")