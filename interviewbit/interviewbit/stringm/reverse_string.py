class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        B = A.split(" ")
        B = [b for b in B if b.strip()]
        return " ".join(B[::-1])
