

class StringPermutation:


	def permute(self, string):

		if len(string) == 1:
			return string

		head = string[0:1]
		tail = string[1::]

		print head
		print tail

		permuteTail = self.permute(tail)

		values = []
		for permutedTail in permuteTail:

			for i in xrange(len(permutedTail)):
				currentHead = permutedTail[0:i]
				currentTail = permutedTail[i:len(permutedTail)]

				aux = currentHead + head + currentTail
				values.append(aux)

			aux = permutedTail + head
			values.append(aux)

		print values

		return values

# StringPermutation().permute("ab")
StringPermutation().permute("abc")