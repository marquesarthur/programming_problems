
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    min_avg_value = (A[0] + A[1]) / 2.0  # The mininal average
    min_avg_pos = 0  # The begin position of the first
    # slice with mininal average
    for index in xrange(0, len(A) - 2):
        # Try the next 2-element slice
        if (A[index] + A[index + 1]) / 2.0 < min_avg_value:
            min_avg_value = (A[index] + A[index + 1]) / 2.0
            min_avg_pos = index
        # Try the next 3-element slice
        if (A[index] + A[index + 1] + A[index + 2]) / 3.0 < min_avg_value:
            min_avg_value = (A[index] + A[index + 1] + A[index + 2]) / 3.0
            min_avg_pos = index
    # Try the last 2-element slice
    if (A[-1] + A[-2]) / 2.0 < min_avg_value:
        min_avg_value = (A[-1] + A[-2]) / 2.0
        min_avg_pos = len(A) - 2

    return min_avg_pos

print(solution([5, 4, -3, 4, -3, 5, -3, 5] ))