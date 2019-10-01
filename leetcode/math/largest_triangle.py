class Solution(object):

    def is_triangle(self, x, y, z):

        return x + y > z and y + z > x and x + z > y




    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        A = sorted(A, reverse=True)
        if len(A) == 3:
            if self.is_triangle(A[0], A[1], A[2]):
                return sum(A)
            else:
                return 0


        for i in range(len(A) - 2):
            if self.is_triangle(A[i], A[i+1], A[i+2]):
                return sum(A[i:i+3])

        return 0



A = [2,1,2] # 5
print(Solution().largestPerimeter(A))

A = [1,2,1] # 0
print(Solution().largestPerimeter(A))

A = [3,2,3,4] # 10
print(Solution().largestPerimeter(A))

A = [3,6,2,3] # 8
print(Solution().largestPerimeter(A))