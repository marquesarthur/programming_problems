def carParkingRoof(cars, k):
    # Write your code here
    # sliding window algorithm. window size = k
    cars = sorted(cars)
    window = cars[0 + k - 1] - cars[0] + 1
    result = window
    for i in xrange(1, len(cars) - k):
        j = i + k - 1
        window = cars[j] - cars[i] + 1
        result = min(result, window)

    return result

# cars, k = [1, 2, 3, 10], 4
# print(carParkingRoof(cars, k)) # 9
#
#
cars, k = [2, 10, 8, 17], 3
print(carParkingRoof(cars, k)) # 9
#
# cars, k = [1, 2, 3, 10, 4], 4
# print(carParkingRoof(cars, k)) # 10

cars, k = [7, 100, 50], 2
print(carParkingRoof(cars, k)) # 44