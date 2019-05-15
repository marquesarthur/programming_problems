# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import re





def row_column(x):
    letters = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'J': 8,
        'K': 9
    }

    row = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", x)
    column = letters[x.replace(row[0], "")]
    return int(row[0]) - 1, int(column)



def max_families_on_row(i, seats):
    row = seats[i]

    if sum(row[1:5]) == 0 and sum(row[5:9]) == 0:
        return 2
    if sum(row[1:5]) == 0 and sum(row[5:9]) > 0:
        return 1
    if sum(row[1:5]) > 0 and sum(row[5:9]) == 0:
        return 1
    if sum(row[3:7]) == 0:
        return 1

    return 0


def solution(N, S):
    max_seats = 0
    seats = [[0 for _ in range(10)] for _ in range(N)]
    for s in S.split(" "):
        i, j = row_column(s)
        seats[i][j] = 1

    for i in range(N):
        max_seats += max_families_on_row(i, seats)

    return max_seats




N = 2
S = '1A 2F 1C'

print(solution(N, S))