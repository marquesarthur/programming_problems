

def spiralOrder(A):
	result = []
	## Actual code to populate result

	top = 0
	bottom = len(A) - 1
	right = len(A[0]) - 1
	left = 0
	
	direction = 0

	while top <= bottom and left <= right:
		print top
		print bottom
		print left
		print right

		if direction == 0:
			for x in range(left, right + 1):
				print "l - r"
				result.append(A[top][x])	

			top = top + 1

		if direction == 1:
			for x in range(top, bottom + 1):
				print "t - b"
				result.append(A[x][right])

			right = right - 1

		if direction == 2 and left - 1 >= 0:
			for x in range(right, left - 1, -1):
				print "r - l"
				result.append(A[bottom][x])

			bottom = bottom - 1

		if direction == 3 and top - 1 >= 0:
			for x in range(bottom, top - 1, -1):
				print "b - t"
				result.append(A[x][left])
			
			left = left + 1

		direction = (direction + 1) % 4


	return result

# Testing inputs/outputs
matrix = [[0 for x in range(3)] for y in range (1)]

matrix[0][0] = 1
matrix[0][1] = 2
matrix[0][2] = 3

# matrix[1][0] = 4
# matrix[1][1] = 5
# matrix[1][2] = 6

# matrix[2][0] = 7
# matrix[2][1] = 8
# matrix[2][2] = 9

print spiralOrder(matrix)


