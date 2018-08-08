
class Solution:
    def justifyLines(self, lines, L):
        result = []
        for line in lines:
            curr = len(" ".join(line))

            if len(line) == 1:
                result.append(line[0] + " " * (L - curr))
            else:
                to_all = (L - curr) // (len(line) - 1)
                additional = (L - curr) % (len(line) - 1)
                res = line.pop(0)

                for word in line:
                    res += " " * (to_all + 1)
                    if additional > 0:
                        res += " "
                        additional -= 1
                    res += word
                result.append(res)
        return result

    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):

        lines = []
        partial = []
        for word in A:
            if len(" ".join(partial + [word])) <= B:
                partial.append(word)
            else:
                lines.append(partial)
                partial = [word]

        if partial:
            lines.append(partial)

        result = self.justifyLines(lines, B)
        return result


# print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
# print(Solution().fullJustify(["What", "must", "be", "shall", "be."], 12))
#
# A = [ "glu", "muskzjyen", "ahxkp", "t", "djmgzzyh", "jzudvh", "raji", "vmipiz", "sg", "rv", "mekoexzfmq", "fsrihvdnt", "yvnppem", "gidia", "fxjlzekp", "uvdaj", "ua", "pzagn", "bjffryz", "nkdd", "osrownxj", "fvluvpdj", "kkrpr", "khp", "eef", "aogrl", "gqfwfnaen", "qhujt", "vabjsmj", "ji", "f", "opihimudj", "awi", "jyjlyfavbg", "tqxupaaknt", "dvqxay", "ny", "ezxsvmqk", "ncsckq", "nzlce", "cxzdirg", "dnmaxql", "bhrgyuyc", "qtqt", "yka", "wkjriv", "xyfoxfcqzb", "fttsfs", "m" ]
# B = 144
#
# s = Solution().fullJustify(A, B)
# print(s[0] == "glu  muskzjyen  ahxkp  t  djmgzzyh  jzudvh  raji  vmipiz  sg rv mekoexzfmq fsrihvdnt yvnppem gidia fxjlzekp uvdaj ua pzagn bjffryz nkdd osrownxj")