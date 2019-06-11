




def find_sum_hash(A, target):


    x = {}
    for i, value in enumerate(A):
        x[value] = i

    for i, value in enumerate(A):

        if (target - value) in x:
            return i, x[target - value]

    return -1



def find_sum(A, target):


    A = sorted(A)


    l = 0
    r = len(A) - 1


    while l != r:

        if A[l] + A[r]  > target:
            r -= 1
        elif A[l] + A[r]  < target:
            l += 1
        else:
            return l, r




    return -1





A = [1, 4, 45, 6, 10, -8]
target = 16


print(find_sum(A, target))
print(find_sum_hash(A, target))


print(find_sum(A, target + 1))
print(find_sum_hash(A, target + 1))



