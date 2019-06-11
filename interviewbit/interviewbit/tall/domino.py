

def split_input(S):
    tiles = S.split(",")

    return [(t.split("-")[0], t.split("-")[1]) for t in tiles]

def match(a, b):
    return a[1] == b[0]

def longest_match(domino_tiles):
    longest = 0
    for i in range(len(domino_tiles)):
        current = 1
        for j in range(i + 1, len(domino_tiles)):
            if match(domino_tiles[j - 1], domino_tiles[j]):
                current += 1
            else:
                break

        longest = max(current, longest)

    return longest



def domino(S):
    domino_tiles = split_input(S)


    return longest_match(domino_tiles)


# print(domino("1-1,3-5,5-2,2-3,2-4"))


print(domino("1-1")) # // 1
print(domino("1-2,1-2")) #// 1
print(domino("5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5")) #// 7
print(domino("3-2,2-1,1-4,4-4,5-4,4-2,2-1")) #// 4
print(domino("1-1,3-5,5-5,5-4,4-2,1-3")) # // 4
print(domino("1-2,2-2,3-3,3-4,4-5,1-1,1-2")) #// 3
