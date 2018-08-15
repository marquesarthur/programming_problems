class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if B == 0:
            return 1 if A != 0 else 0
        if B == 1:
            return A % C
        if B < 0:
            return (1.0 / self.Mod(A, abs(B), C)) % C

        if B % 2 == 0:
            x = self.Mod(A, int(B / 2), C)
            return (x * x) % C
        else:
            return (A * self.Mod(A, B - 1, C)) % C
