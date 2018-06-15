class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
	def diagonal(self, a):
		m = len(a)
		n = len(a[0])
		result = []
		
		# superior diagonal
		for i in xrange(m):
			partial = []
			self.appendDiagonal(a, 0, i, partial)
			result.append(partial)

		for i in xrange(1, m):
			partial = []
			self.appendDiagonal(a, i, n - 1, partial)
			result.append(partial)

		return result

	# inferior diagonal
	def appendDiagonal(self, a, i, j, current):
		m = len(a)
		n = len(a[0])

		if (i >= 0 and i < m and j >= 0 and j < n):
			current.append(a[i][j])
			self.appendDiagonal(a, i + 1, j - 1, current)
		else:
			return
		



assert(Solution().diagonal([[1]]) == [[1]])
assert(Solution().diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1], [2, 4], [3, 5, 7], [6, 8], [9]])