class Solution:
    def sumEvenAfterQueries(self, A, queries):
        result = [0 for _ in range(len(A))]
        i = 0
        current = 0
        for value, idx in queries:
            before = A[idx]
            A[idx] += value
            after = A[idx]
            if i == 0:
                current = sum([k for k in A if k % 2 == 0])
                result[i] = current
            else:
                if before % 2 == 0 and after % 2 == 0:
                    current += (after - before)
                elif before % 2 == 0 and after % 2 == 1:
                    current -= before
                elif before % 2 == 1 and after % 2 == 0:
                    current += after

                result[i] = current

            i += 1

        return result




A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
print(Solution().sumEvenAfterQueries(A, queries))