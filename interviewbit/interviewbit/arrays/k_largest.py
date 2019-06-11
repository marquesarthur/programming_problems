


def k_largest_temp(k, A):
    result = []

    if not A or not k:
        return result

    if len(A) <= k:
        return A



    result = A[:k]
    min_a = min(result)
    j = A.index(min_a)


    for i in range(k, len(A)):
        if A[i] > min_a:
            result.pop(j)
            result.append(A[i])
            min_a = min(result)
            j = result.index(min_a)

    return sorted(result)


def k_largest(k, A):
    result = []

    if not A:
        return result

    if len(A) <= k:
        return A

    A = sorted(A, reverse=True)

    return sorted(A[:k])





A = [1, 23, 12, 9, 30, 2, 50]


print(k_largest(3, A))
print(k_largest_temp(3, A))
print()
print(k_largest(4, A))
print(k_largest_temp(4, A))
print()
print(k_largest(0, A))
print(k_largest_temp(0, A))
print()
print(k_largest(100, A))
print(k_largest_temp(100, A))
print()


