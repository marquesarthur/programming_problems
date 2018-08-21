class Solution:
    # @param A : list of integers
    # @return an integer
    def deleteandconquer(self, A):
        if not A:
            return 0

        num_count = {}
        for i in A:
            if i not in num_count:
                num_count[i] = 0
            num_count[i] += 1

        _max_count = 0
        for k in num_count.keys():
            if num_count[k] > _max_count:
                _max_count = num_count[k]

        return len(A) - _max_count
