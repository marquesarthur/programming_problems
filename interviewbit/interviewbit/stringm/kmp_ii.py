class KMP(object):



    def init(self, A):
        ret = [0]

        for i in range(1, len(A)):
            j = ret[i - 1]
            while j > 0 and A[i] != A[j]:
                j = ret[j - 1]
            result = j + 1 if A[i] == A[j] else j
            ret.append(result)

        return ret

    def find_substr(self, A, B):
        partial, result, j = self.init(B), [], 0

        for i in range(len(A)):
            while j > 0 and A[i] != B[j]:
                j = partial[j] - 1

            if A[i] == B[j]:
                j += 1

            if j == len(B):
                result.append(i - (j - 1))
                j = 0

        return result


print(KMP().init("AABC"))
print(KMP().init("AACAA"))

print(KMP().find_substr("AABCXAABCKIAA", "AABC"))

