

def recursively_count(num):
    if num == 0:
        return 0
    if int(num / 2) == 0:
        return num % 2
    else:
        x = int(num / 2)
        y = num % 2
        return recursively_count(x) + recursively_count(y)

def count_ones(num):
    return recursively_count(num)


def count_ones_non_recursive(num):
    count = 0
    while int(num / 2) > 0:
        mod = num % 2
        num = int(num / 2)
        if mod != 0:
            count += 1

    if num % 2 > 0:
        count += 1

    return count



print(count_ones(4))
print(count_ones(5))
print(count_ones(3))


print(count_ones_non_recursive(4))
print(count_ones_non_recursive(5))
print(count_ones_non_recursive(3))



