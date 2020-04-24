

class Solution:
    def reconstructQueue(self, people):

        stack = []

        for p in people:
            h, k = p[0], p[1]

            if not stack:
                stack.append(p)
            else:
                taller_than_me = [idx for idx, x in enumerate(stack) if x[0] >= h]
                aux = []
                while len(taller_than_me) > k and stack:
                    aux.append(stack.pop())
                    taller_than_me -= 1
                stack.append(p)
                if aux:
                    stack += aux


        return stack



people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
print(Solution().reconstructQueue(people))


# sort by height?
# 4, 5, 5, 6, 7, 7
