class KMP(object):

    def partial(self, pattern):
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)

        return ret


    def search(self, pattern, str):

        partial, ret, j = self.partial(pattern), [], 0

        for i in range(len(str)):
            while j > 0 and str[i] != pattern[j]:
                j = partial[j - 1]
            if str[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                ret.append(i - (j - 1))
                j = 0

        return ret
