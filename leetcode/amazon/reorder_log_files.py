
def compare_letter_logs(a, b):
    x = a[a.index(" ") + 1:].split(" ")
    y = b[b.index(" ") + 1:]. split(" ")

    for xi, yj in zip(x, y):
        if xi < yj:
            return -1
        if yj < xi:
            return 1

    return 0



class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        letters = []
        digits = []
        for l in logs:
            if l.split(" ", 1)[0].startswith("let"):
                letters.append(l)
            else:
                digits.append(l)

        letters = sorted(letters, cmp=compare_letter_logs)

        return letters + digits






logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
expected = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

print(Solution().reorderLogFiles(logs))