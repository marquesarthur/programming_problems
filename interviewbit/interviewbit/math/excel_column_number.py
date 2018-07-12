import string

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        A = A.upper()
        aux = string.ascii_uppercase
        letters = list(aux)

        result = 0
        n = 0
        for value in reversed(list(A)):
            i = letters.index(value) + 1
            result += i * (len(letters)**n)
            n += 1

        return result