class Solution:

    def is_palin(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

    def rec_part(self, string, idx, t, ans):
        if idx == len(string):
            ans.append(t[:])
        else:
            for str_size in xrange(idx, len(string)):
                p = string[idx:str_size + 1]
                if self.is_palin(p):
                    t.append(p)
                    self.rec_part(string, str_size + 1, t, ans)
                    t.pop()

    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        ans = []
        self.rec_part(A, 0, [], ans)
        return ans


print(Solution().partition("efe"))
