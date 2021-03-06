class Solution:

    def __is_palindrome(self, string):
        if not string:
            return False

        i = 0
        j = len(string) - 1

        while i < j:
            if string[i] != string[j]:
                return False

            i += 1
            j -= 1

        return True

    def __partition(self, partial, A, i, j, n):
        if i < len(A):
            partition = A[i:j]
            if self.__is_palindrome(partition):
                partial.append(partition)
                self.__partition(partial, A, j, j + n, n)
            else:
                self.__partition(partial, A, i, j - 1, n)




    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        if not A:
            return []

        # 1 walk until length is n
        # for each pair store tuple, (begin, end, str)
        # when at a[i] recursively match new tuples

        # base case:
        partial = tuple([A[i] for i in range(len(A))])
        result = [partial]
        result = set(result)

        for i in range(2, len(A) + 1):
            partial = []
            j = 0
            k = j + i
            self.__partition(partial, A, j, k, i)
            partial = tuple(partial)
            if partial and partial not in result:
                result.add(partial)


        return sorted([list(a) for a in result], key=len, reverse=True)




print(Solution().partition("efe"))