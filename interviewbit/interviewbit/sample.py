def read_input():
    numbers_count = int(input())
    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input())
        numbers.append(str(numbers_item))

    list.reverse(numbers)
    print('\n'.join(numbers))


if __name__ == '__main__':
    read_input()
