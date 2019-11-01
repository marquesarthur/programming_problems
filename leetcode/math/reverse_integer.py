class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            y = str(x)[::-1]
        else:
            y = str(x)[1:len(str(x))][::-1]
        x = int(y) if x > 0 else -int(y)

        _min = -2 ** 31
        _max = 2 ** 31 - 1

        if _min <= x <= _max:
            return x
        return 0