import heapq
import math


import heapq
class SolutionOptimal:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        chox = []
        total_chocs = 0
        #insert chox into heap as -ve so as to get max on heappop
        for i in xrange(len(B)):
            heapq.heappush(chox, ((B[i])*-1))
        for i in xrange(A):
             current_max = heapq.heappop(chox)*-1
             total_chocs += current_max
             heapq.heappush(chox, ((current_max/2)*-1))
        return total_chocs%((10**9)+7)


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        h = []
        for val in B:
            heapq.heappush(h, -val)

        sum = 0
        for i in xrange(A):
            maxitem = abs(heapq.heappop(h))

            sum += maxitem
            sum = sum % (10**9+7)

            new_item = int(math.floor(maxitem / 2.0))
            heapq.heappush(h, -new_item)

        return sum % (10**9+7)

print(Solution().nchoc(3, [6, 5]))

