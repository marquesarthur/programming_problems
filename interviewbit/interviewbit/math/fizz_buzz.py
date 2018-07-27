class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        result = []
        for i in len(range(A)):
            if A[i] % 5 == 0 and A[i] % 3 == 0:
                result.append("FizzBuzz")
            elif A[i] % 5 == 0:
                result.append("Buzz")
            elif A[i] % 3 == 0:
                result.append("Fizz")
            else:
                result.append(A[i])
        return result
