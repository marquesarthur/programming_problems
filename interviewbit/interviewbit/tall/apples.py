# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

C = 1000000007


def max_sum_in(arr, L):

    result = 0

    for i in range(0, len(arr)):

        if len(arr[i:L]) == L:
            current = sum(arr[i:i+L]) % C
            result = max(current, result)

    return result % C




def get_other_slices(A, B, L):

    pre = 0
    post = 0
    if len(A) >= L:
        pre = max_sum_in(A, L)

    if len(B) >= L:
        post = max_sum_in(B, L)

    return max(pre, post) % C




def solution(A, K, L):
    # write your code in Python 3.6



    if K + L > len(A):
        return -1

    max_result = 0
    n = len(A)
    for i in range(0, n):
        alice_apples = A[i:i+K]
        alice = sum(alice_apples) % C
        bob_apples = get_other_slices(A[:i], A[i+K + 1:], L)


        max_result = max(alice + bob_apples, max_result)
        max_result = max_result % C


    return max_result


print(solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2))


print(solution([10, 19, 15], 2, 2))