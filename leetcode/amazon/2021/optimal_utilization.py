
from bisect import bisect_left, bisect_right

def optimal_utilization(lst_a, lst_b, target):
    result = []

    lst_a = sorted(lst_a, key=lambda k: k[1])
    lst_b = sorted(lst_b, key=lambda k: k[1])

    values_lst_b = [k[1] for k in lst_b]


    for elem in lst_a:

        _id_a, value_a = elem[0], elem[1]

        target_value = target - value_a

        idxs = bisect_right(values_lst_b, target_value)

        # bisect.bisect_left returns the leftmost place in the sorted list to insert the given element.
        # bisect.bisect_right returns the rightmost place in the sorted list to insert the given element




        if idxs > 0:
            idxs -= 1 # right most place, so value will be one to the lft, hence -1

            __elem = lst_b[idxs]
            _id_b, value_b = __elem[0], __elem[1]
            current_sum = value_a + value_b

            if current_sum <= target:
                if not result:
                    result.append((current_sum, _id_a, _id_b))
                else:

                    while result and current_sum > result[-1][0]:
                        result.pop()
                    result.append((current_sum, _id_a, _id_b))



    ids = [[a, b] for _, a,b in result]
    return ids


a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

print('')
print('Output = [[2, 1]]')
print(optimal_utilization(a, b, target))



a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

print('')
print('Output: [[2, 4], [3, 2]]')
print(optimal_utilization(a, b, target))


a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20
print('')
print('Output: [[3, 1]]')
print(optimal_utilization(a, b, target))


a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20
print('')
print('Output: [[1, 3], [3, 2]]')
print(optimal_utilization(a, b, target))