import sys


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """



        if not triangle:
            return 0

        if len(triangle) == 1:
            return triangle[0][0]



        # In place removal
        min_path = sys.maxint
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):

                if j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                elif j == 0:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i - 1][j - 1],  triangle[i - 1][j]) + triangle[i][j]

                if i == len(triangle) - 1:
                    min_path = min(min_path,triangle[i][j] )



        return  min_path










triangle = [[2]]
print(Solution().minimumTotal(triangle))


#
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))
#

triangle = [
     [2],
    [3,4],
   [9,10,2]
]
print(Solution().minimumTotal(triangle))


triangle = [
     [2],
    [3,4],
   [9,10,2]
]
print(Solution().minimumTotal(triangle))

triangle = [
     [2],
    [3,4],
   [9,10,2],
[4, 1, 50, 50]
]
print(Solution().minimumTotal(triangle))