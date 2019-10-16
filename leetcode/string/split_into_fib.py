class Solution(object):

    def is_valid(self, value):
        if int(value) > 2**31 - 1:
            return False

        if "0" not in value:
            return True
        elif value.index("0") == 0 and len(value) == 1:
            return True
        elif value.index("0") != 0 and len(value) > 1:
            return True
        else:
            return False


    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]

        """
        if not S:
            return []
        if len(S) <= 2:
            return []

        all_is = []
        for i in xrange(1, len(S) - 2):
            all_is.append(i)

        for i in all_is:
            for j in xrange(i + 1, len(S)):
                a = S[0:i]
                b = S[i: j]
                aux = str(S)

                if self.is_valid(a) and self.is_valid(b):
                    aux = aux.replace(a, "", 1)
                    aux = aux.replace(b, "", 1)
                    fib = [int(a), int(b)]
                    k = 1
                    next = str(fib[k - 1] + fib[k])

                    while aux and self.is_valid(next) and next in aux and aux.index(next) == 0:
                        fib.append(int(next))
                        aux = aux.replace(next, "", 1)
                        k += 1
                        next = str(fib[k - 1] + fib[k])

                    if len(aux) == 0:
                        return fib

        return []







Input = "123456579"
Output = [123,456,579]
print(Solution().splitIntoFibonacci(Input))
#
#
# Input = "11235813"
# Output = [1,1,2,3,5,8,13]
# print(Solution().splitIntoFibonacci(Input))
#
#
# Input = "112358130"
# Output = []
# print(Solution().splitIntoFibonacci(Input))
#
#
# Input = "0123"
# Output = []
# print(Solution().splitIntoFibonacci(Input))
#
# Input = "1101111"
# Output = [110, 1, 111]
# print(Solution().splitIntoFibonacci(Input))
#
# Input = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
# print(Solution().splitIntoFibonacci(Input))