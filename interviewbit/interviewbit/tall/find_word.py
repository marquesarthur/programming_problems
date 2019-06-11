#
#
#
#
#
#
#
#
# def insert_character(word, new_letter, before):
#
#     if new_letter in word:
#         return word
#
#     result = ""
#     for c in word:
#         if c == before:
#             result = new_letter + c
#         else:
#             result = result + c
#
#     if new_letter not in result:
#         result += new_letter
#
#     return result
#
#
#
#
#
# def findWord(rules):
#     rules = sorted(rules, cmp=sort_by_rules)
#     word = ""
#     for r in rules:
#         left, right = r.split(">")[0], r.split(">")[1]
#
#         if not word:
#             word = left+right
#         else:
#             word = insert_character(word, left, right)
#             word = insert_character(word, right, right)
#     return word
#
#
#
# # print(findWord(["P>E","E>R","R>U"])) # // PERU
# # print(findWord(["I>N","A>I","P>A","S>P"])) # // SPAIN
# #
# # print(findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"])) # // HUNGARY
# # print(findWord(["I>F", "W>I", "S>W", "F>T"])) # // SWIFT
# # print(findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"])) # // SWITZERLAND
# print(findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]))  #// PORTUGAL
