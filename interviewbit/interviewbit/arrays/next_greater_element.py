

# Worst case is O(n^2) but avg case is O(n log n)
def next_greater_element(A):
    B = [(i, x) for i, x in enumerate(A)]

    B = sorted(B, key=lambda k: k[1])
    result = [-1 for _ in A]

    for i in range(len(B)):
        idx, value = B[i]
        idx_j, value_j = None, None
        for j in range(i + 1, len(B)):
            if B[j][1] > value and B[j][0] > idx:
                idx_j, value_j = B[j]
                break

        if idx_j and value_j:
            result[idx] = value_j

    return result


A = [4, 5, 2, 25]
expected = [5, 25, 25, -1]

print(expected == next_greater_element(A))
