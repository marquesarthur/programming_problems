import functools


def compare_restaurants(a, b):
    if a.rating < b.rating:
        return -1
    elif a.rating > b.rating:
        return 1
    elif a.id < b.id:
        return -1
    elif a.id > b.id:
        return 1
    else:
        return 0


class Restaurant(object):

    def __init__(self, data):
        self.id = data[0]
        self.rating = data[1]
        self.veganFriendly = data[2]
        self.maxPrice = data[3]
        self.maxDistance = data[4]


class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        for i in range(len(restaurants)):
            restaurants[i] = Restaurant(restaurants[i])

        if veganFriendly == 1:
            result = list(filter(
                lambda k: k.veganFriendly == veganFriendly and k.maxPrice <= maxPrice and k.maxDistance <= maxDistance,
                restaurants))
        else:
            result = list(filter(lambda k: k.maxPrice <= maxPrice and k.maxDistance <= maxDistance, restaurants))

        result = sorted(result, key=functools.cmp_to_key(compare_restaurants), reverse=True)

        return [r.id for r in result]
