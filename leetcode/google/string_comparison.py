import string

letters = list(string.ascii_lowercase)


class Solution():

    def compare(self, A, B):

        M = A.split(" ")
        N = B.split(" ")

        M_character_count = []
        N_character_count = []

        for m in M:
            count = {c: 0 for c in letters}
            for c in m:
                count[c] += 1

