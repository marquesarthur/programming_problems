import re


class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        if not A:
            return 0

        A = A.strip()
        integer_re = re.compile(r'^[-+]?[0-9]+$')
        float_re = re.compile(r'^[-+]?([0-9]+)?\.[0-9]+$')
        scientific_notation_re = re.compile(r'^[-+]?[0-9]+(\.[0-9]+)?e[-+]?[0-9]+$')

        has_integer = integer_re.findall(A)
        has_float = float_re.findall(A)
        has_scientific_notation = scientific_notation_re.findall(A)

        if len(has_float) > 0 or len(has_integer) > 0 or len(has_scientific_notation) > 0:
            return 1
        else:
            return 0


print(Solution().isNumber("0"))
print(Solution().isNumber("0.1"))
print(Solution().isNumber("2e10"))
print(Solution().isNumber("0.1e10"))
print(Solution().isNumber("-01.1e-10"))
print(Solution().isNumber("0"))
print(Solution().isNumber("00"))
print(Solution().isNumber("008"))
print()
#
print(Solution().isNumber("abc"))  # false
print(Solution().isNumber("1 a"))  # false
print(Solution().isNumber("3."))  # fasle
print(Solution().isNumber("1f"))
print(Solution().isNumber("1000LL"))
print(Solution().isNumber("1000L"))
print(Solution().isNumber("3e0.1"))
