
import random

def findMostToLeft(precedence_map, letters):
    # pick a random key in the map
    keys = set(precedence_map.values())
    last_letter = letters.difference(keys)
    last_letter = next(iter(last_letter))
    return last_letter


def findWord(rules):
    precedence_map = {}
    letters = set()
    for r in rules:
        left, right = r.split(">")[0], r.split(">")[1]
        precedence_map[left] = right
        letters.add(left)
        letters.add(right)

    letter = findMostToLeft(precedence_map, letters)

    result = []
    while letter in precedence_map:
        result.append(letter)
        letter = precedence_map[letter]

    result.append(letter)



    return "".join(result)




print(findWord(["P>E","E>R","R>U"])) # // PERU
print(findWord(["I>N","A>I","P>A","S>P"])) # // SPAIN
print(findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"])) # // HUNGARY
print(findWord(["I>F", "W>I", "S>W", "F>T"])) # // SWIFT
print(findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"])) # // SWITZERLAND
print(findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]))  # // PORTUGAL
