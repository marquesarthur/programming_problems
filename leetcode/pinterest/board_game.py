board = [
    [0,  0,  0,  0,  0,  0, -1],
    [0,  0,  0, -1,  0,  0,  0],
    [0,  0, -1,  0, -1,  0,  0],
    [-1, 0, -1,  0,  0,  0,  0],
    [0,  0, -1,  0,  0,  0,  0],
    [0,  0,  0,  0,  0, -1,  0],
]

board_smaller = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

board_unreachable = [
    [0, -1, 0],
    [-1, 0, -1],
    [0, -1, 0],
]

WALL = -1


def valid_moves(board, position):
    row, column = position

    steps = [
        (-1, 0),  # row before
        (+1, 0),  # row after
        (0, -1),  # column before
        (0, +1)   # column after
    ]

    n, m = len(board), len(board[0])
    valid_moves = []
    for i, j in steps:

        if 0 <= row + i < n and 0 <= column + j < m:
            if board[row + i][column + j] != WALL:
                valid_moves.append((row + i, column + j))

    return valid_moves


print("Unreachable board")
print(valid_moves(board_unreachable, (0, 0)))
print(valid_moves(board_unreachable, (0, 2)))
print(valid_moves(board_unreachable, (2, 0)))
print(valid_moves(board_unreachable, (2, 2)))


print("Reachable board")
print(valid_moves(board_smaller, (0, 0)))
print(valid_moves(board_smaller, (0, 2)))
print(valid_moves(board_smaller, (2, 0)))
print(valid_moves(board_smaller, (2, 2)))
print(valid_moves(board_smaller, (1, 1)))



def traverse(board, current, visited):
    if current in visited:
        return
    else:
        visited.add(current)
        moves = valid_moves(board, current)
        for m in moves:
            traverse(board, m, visited)



def is_reachable(board, end_position):
    n, m = len(board), len(board[0])
    all_positions = set()
    for i in xrange(n):
        for j in xrange(m):
            if board[i][j] != WALL:
                all_positions.add((i, j))

    visited = set()
    traverse(board, end_position, visited)

    for p in all_positions:
        if p not in visited:
            return False

    return True

print
print
print("Unreachable board")
print(is_reachable(board_unreachable, (0, 0)))
print(is_reachable(board_unreachable, (0, 2)))
print(is_reachable(board_unreachable, (2, 0)))
print(is_reachable(board_unreachable, (2, 2)))


print
print
print("Reachable boards")
print(is_reachable(board_smaller, (0, 0)))
print(is_reachable(board, (0, 2)))




TREASURE = 8



def traverse_to(board, current, end,  visited, treasures, solutions):
    if current in visited:
        return
    elif current == end:
        new_visit = list(visited)
        new_visit.append(current)
        treasures_in_path = list(filter(lambda k: k in treasures, new_visit))
        if len(treasures_in_path) == len(treasures):
            solutions.append(new_visit)
            return
        else:
            return
    else:

        new_visit = list(visited)
        new_visit.append(current)
        moves = valid_moves(board, current)
        for m in moves:
            traverse_to(board, m, end, new_visit, treasures, solutions)


def treasure_hunt(board, start, end):
    n, m = len(board), len(board[0])
    treasures = set()
    for i in xrange(n):
        for j in xrange(m):
            if board[i][j] == TREASURE:
                treasures.add((i, j))

    visited = list()
    solutions = list()
    traverse_to(board, start, end, visited, treasures, solutions)

    if not solutions:
        return []

    min_path = min([len(k) for k in solutions])
    min_paths = list(filter(lambda k: len(k) == min_path, solutions))

    return min_paths



board = [
    [0,  0,  8,  0,  0,  0, -1],
    [0,  0,  0, -1,  8,  0,  0],
    [0,  0, -1,  0, -1,  0,  0],
    [-1, 0, -1,  0,  0,  0,  0],
    [0,  0, -1,  8,  0,  0,  0],
    [0,  0,  0,  0,  0, -1,  0],
]

board_smaller = [
    [8, 0, 0],
    [0, 8, 0],
    [0, 0, 0],
]

print
print
print("Treasure hunt")
print("\n".join(["path --> " + str(k) for k in treasure_hunt(board_smaller, (0, 0), (2, 2))]))
print
print
print("Treasure hunt")
print("\n".join(["path --> " + str(k) for k in treasure_hunt(board, (0, 0), (2, 2))]))
print
print
print("Treasure hunt")
print("\n".join(["path --> " + str(k) for k in treasure_hunt(board, (0, 0), (5, 3))]))





def treasure_hunt_print_path(board, start, end):
    print("Treasure hunt")
    n, m = len(board), len(board[0])
    treasures = set()
    for i in xrange(n):
        for j in xrange(m):
            if board[i][j] == TREASURE:
                treasures.add((i, j))

    visited = list()
    solutions = list()
    traverse_to(board, start, end, visited, treasures, solutions)

    if not solutions:
        print("no luck")

    min_path = min([len(k) for k in solutions])
    min_paths = list(filter(lambda k: len(k) == min_path, solutions))


    for path in min_paths:
        print
        print("Hey I found a path")
        print
        for i in xrange(n):
            line = list(board[i])
            for j, value in enumerate(line):
                if (i, j) in path:
                    line[j] = "X"
                else:
                    line[j] = str(value)

            print(line)


treasure_hunt_print_path(board_smaller, (0, 0), (2, 2))

print
print

treasure_hunt_print_path(board, (0, 0), (5, 3))