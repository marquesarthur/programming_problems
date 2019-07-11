

# Brute force approach!
def findWord(rules):
    precedence_map = {}
    letters = set()
    for r in rules:
        left, right = r.split(">")[0], r.split(">")[1]
        precedence_map[left] = right
        if right not in precedence_map:
            precedence_map[right] = precedence_map[left]
        letters.add(left)
        letters.add(right)

    stack = list(letters)

    iterations = 0

    while iterations <= 1000:

        for letter, before in precedence_map.items():

            if letter != before:
                stack.pop(stack.index(letter))
                stack.insert(stack.index(before), letter)

        iterations += 1

        # if letter in inverse_precedence_map:
        #     recursive_insert_left(stack, letter, inverse_precedence_map[letter])

    return "".join(stack)


# print(findWordRecursive(["P>E","E>R","R>U"])) # // PERU
# print(findWord(["I>N","A>I","P>A","S>P"])) # // SPAIN
#
# print(findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"])) # // HUNGARY
# print(findWord(["I>F", "W>I", "S>W", "F>T"])) # // SWIFT
# print(findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"])) # // SWITZERLAND
print(findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]))  # // PORTUGAL
