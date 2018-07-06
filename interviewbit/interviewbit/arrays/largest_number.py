def compare(x, y):
    v = long(str(x) + str(y))
    w = long(str(y) + str(x))
    if v > w:
        return 1
    elif v < w:
        return -1
    else:
        return 0


class Solution:
    def sort_values(self, values):
        return sorted(values, cmp=compare, reverse=True)

    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        _str = ""
        for key in self.sort_values(A):
            _str += str(key)

        while _str[0] == '0' and len(_str) > 1:
            _str = _str[1:len(_str)]

        return _str
