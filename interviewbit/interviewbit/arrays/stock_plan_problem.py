
from bisect import bisect_right



def stock_plan(A):
    result = [1 for _ in A]


    # create array with value and indexes
    # sort array
    # increment the value for every j < i where b[j] <= b[i]


    B = [(i, x) for i, x in enumerate(A)]
    B = sorted(B, key=lambda k: (k[1], k[0]))

    k = 0
    for j, value in B:
        days = [i[0] for i in B[:k]]
        print(j, value)

        days_before = bisect_right(days, j)
        value = 0
        for i in range(days_before, 0, -1):
            if A[i] > value:
                break
            value += 1

        result[j] = max(1, value)






    return result





A = [100, 80, 60, 70, 60, 75, 85]
expected = [1, 1, 1, 2, 1, 4, 6]


print(expected == stock_plan(A))