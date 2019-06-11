
from bisect import bisect_right
from bisect import bisect_left




def has_pythagorean_triplet(A):

    A = sorted(A)
    A = [i**2 for i in A]


    for i in range(len(A)):
        for j in range(i + 1, len(A)):

            target = A[i] + A[j]
            if target in A:
                return True



    return False






a = [3, 1, 4, 6, 5]
b = [10, 4, 6, 12, 5]


print(has_pythagorean_triplet(a))
print(has_pythagorean_triplet(b))