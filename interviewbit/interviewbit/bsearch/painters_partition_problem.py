import math


class Solution:
    def get_sums_time(self, arr):
        result = set()
        for i in range(len(arr)):
            result.add(arr[i])
            for j in range(i, len(arr) + 1):
                result.add(sum(arr[i:j]))

        return sorted(list(result))

    # for each entry pick a painter and assign to him C[i:j] <= min_T repeat
    # I have to be careful here. The min i:j has to be equal to math.ceil(len(C) / K)
    def painters_can_do_job(self, K, T, current_min_time):

        # k = 2
        # 5 10 15
        # current_min_time = 15
        assigned_painters = 0
        i = 0
        while i < len(T):
            current_sum = T[i]
            if current_sum > current_min_time:
                break

            j = i + 1
            _next = j  # 3
            while j < len(T) and current_sum + T[j] <= current_min_time:
                current_sum += T[j]  # 15
                _next = j + 1  # 2
                j += 1

            assigned_painters += 1  # 2
            i = _next

            if assigned_painters == K:
                break

        # I am not 100% sure here. What if I do the job with less painters than
        # K. Some painters will just be iddle. Is that fine?
        return i == len(T)

    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        CONST = 10000003
        K = A  # represent the paintes
        T = B  # represents the time

        T_delta = [(T * i) % CONST for i in C]

        # 1st find minimum time in C
        _min = min(T_delta)
        # 2nd find maximum time in C
        _max = sum(T_delta) % CONST

        # 3rd create array min_T from min to max increasing values by T
        # There mustbe a way to create a smaller interval, but let's try this one first

        min_time = self.get_sums_time(T_delta)

        # min_time = sorted(min_time)

        result = _max

        # 4th binary search in min_T
        begin = 0
        end = len(min_time) - 1

        while begin <= end:
            mid = int((begin + end) / 2)

            current_min_time = min_time[mid]

            if self.painters_can_do_job(K, T_delta, current_min_time):
                result = min(result, current_min_time)
                end = mid - 1
            else:
                begin = mid + 1

        return result


A = 4
B = 10
# C = [884, 228, 442, 889]
# expected = 8890

A = 3
B = 10
C = [ 640, 435, 647, 352, 8, 90, 960, 329, 859 ]
expected = 17220

A = 10
B = 10
C = [ 753, 143, 207, 4, 823 ]
expected = 8230


r = Solution().paint(A, B, C)
print(r)
print(r == expected)
