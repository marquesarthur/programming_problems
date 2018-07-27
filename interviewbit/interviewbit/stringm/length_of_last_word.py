class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if not A:
            return 0

        A = A.strip()
        if not A:
            return 0

        stack = []
        last_word_idx = -1
        for i in range(len(A)):
            if A[i] == " ":
                word = A[last_word_idx + 1: i]
                stack.append(word)
                last_word_idx = i

            if i + 1 == len(A):
                word = A[last_word_idx + 1: i + 1]
                stack.append(word)

        return len(stack.pop())
