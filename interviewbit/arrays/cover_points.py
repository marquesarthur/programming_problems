
def coverPoints(X, Y):
	totalJumps = 0

	for i in xrange(1, len(X) - 1):
		#print "from (%s %s) to (%s %s)" %(X[i], Y[i], X[i + 1], Y[i + 1])
		currentX = X[i]
		currentY = Y[i]

		nextX = X[i + 1]
		nextY = Y[i + 1]

		# jumps from p1 to p2
		xJumps = abs(currentX - nextX)
		yJumps = abs(currentY - nextY)

		# print "\n >>>> %s %s \n" %(xJumps, yJumps)
		totalJumps += max(xJumps, yJumps)
	
	return totalJumps

# Testing inputs/outputs
print coverPoints([1, 0], [1, 0])
print coverPoints([2, 0, 0], [2, 0, 1])
print coverPoints([2, 0, 2], [2, 0, 2])
print coverPoints([3, 0, 1, 1], [3, 0, 1, 2])