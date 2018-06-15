


class MergeSort:

	def merge(self, left, right, A):

		i = 0
		j = 0
		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				A[k] = left[i]
				i += 1
				k += 1
			else:
				A[k] = right[j]
				j += 1
				k += 1

		while i < len(left):
			A[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			A[k] = right[j]
			j += 1
			k += 1

		return A

	def sort(self, A):
		if len(A) == 1:
			return A

		mid = len(A) / 2

		left = []
		right = []

		for i in xrange(0, mid):
			left.append(A[i])

		for j in xrange(mid, len(A)):
			right.append(A[j])

		self.sort(left)
		self.sort(right)

		self.merge(left, right, A)

		print A

		return A

MergeSort().sort([6, 2, 9, 4 , 5, 13, 50, 33, 31, 45, 62, 16, 18, 21, 13])


