def convert_input(n, m, input):
    result = [[0 for x in range(n)] for y in range(m)]

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "X":
                result[i][j]= "X"


    return result


def count_nearby(n, m, matrix):
    for i in range(n):
        for j in range(m):

            num_of_mines = matrix[i][j]
            if matrix[i][j] != "X":

                if i - 1 >= 0: # line before
                    if j - 1 >= 0 and matrix[i-1][j-1] == "X": # column before
                        num_of_mines += 1

                    if j  >= 0 and matrix[i-1][j] == "X": # column before
                        num_of_mines += 1

                    if j + 1 < m and matrix[i-1][j+1] == "X": # column before
                        num_of_mines += 1


                if j - 1 >= 0 and matrix[i][j - 1] == "X":  # column before
                    num_of_mines += 1



                if j + 1 < m and matrix[i][j + 1] == "X":  # column before
                    num_of_mines += 1

                if i + 1 < n:  # line after
                    if j - 1 >= 0 and matrix[i+1][j - 1] == "X":  # column before
                        num_of_mines += 1

                    if j  >= 0 and matrix[i+1][j] == "X":  # column before
                        num_of_mines += 1

                    if j + 1 < m and matrix[i+1][j + 1] == "X":  # column before
                        num_of_mines += 1

                matrix[i][j] = num_of_mines





def minesweeper(input):


    n = len(input)

    if n == 0:
        return []

    m = len(input[0])

    matrix = convert_input(n, m, input)
    count_nearby(n, m, matrix)





    return matrix


def main():
    minesweeper(["XOO", "OOO", "XXO"])


if __name__ == "__main__":
    main()

