# def all_idx_combinations(_nexts, _idx, result, current, target, n_students):
#
#     if len(current) == target:
#         result.append(current)
#
#     for k in _nexts:
#
#
#         aux = list(current + [A[k[0]: k[1]]])
#         if k[1] == target and len(aux) == n_students:
#             result.append(aux)
#         elif k[1] in _idx:
#             _next_next = _idx[k[1]]
#             all_idx_combinations(_next_next, _idx, result, aux, target, n_students)
#
#
# def sliding_window(A, target, n_students):
#     start,end = 0, 0
#
#     combinations = set()
#
#     n = len(A)
#     while end <= n:
#
#         if sum(A[start:end]) <= target:
#             combinations.add((start, end))
#             end += 1
#         else:
#             if sum(A[start:end-1]) <= target:
#                 combinations.add((start, end))
#             start += 1
#
#     combinations = sorted(combinations, key=lambda k: k[0])
#
#     _idx = { }
#     for k in combinations:
#         start = k[0]
#         if start not in _idx:
#             _idx[start] = []
#
#         _idx[start].append(k)
#
#
#
#     result = []
#     for k in _idx[0]:
#         if k[1] != k[0] and k[1] in _idx:
#             current = [A[k[0]: k[1]]]
#             _next = _idx[k[1]]
#             all_idx_combinations(_next, _idx, result, current, len(A), n_students)
#
#     _max = sum(A)
#     idx = -1
#     for i, partial in enumerate(result):
#         sums = [sum(i) for i in partial]
#         aux = max(sums)
#         if aux < _max:
#             idx = i
#             _max = aux
#
#     if idx != -1:
#         return result[idx]
#     return -1


class Solution:
    def can_students_read_books(self, A, B, n_pages):

        if n_pages < max(A):
            return False

        _sum, assigned_students = 0, 0

        for current in A:

            if _sum + current <= n_pages:
                _sum += current
            else:
                assigned_students += 1
                if assigned_students >= B:
                    return False
                _sum = current

        return True

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if len(A) < B:
            return -1

        _min_pages = min(A)
        _max_pages = sum(A)

        result = -1
        while _min_pages <= _max_pages:

            _mid = int((_min_pages + _max_pages) / 2)

            aux = self.can_students_read_books(A, B, _mid)

            if aux:
                result = _mid
                _max_pages = _mid - 1
            else:
                _min_pages = _mid + 1

        return result


A = [73, 58, 30, 72, 44, 78, 23, 9]
B = 5
expected = 110

r = Solution().books(A, B)
print(r)
print(r == expected)
