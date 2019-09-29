class Solution(object):
    """
    The intuition behind this approach is that the area formed between the lines will always
    be limited by the height of the shorter line. Further, the farther the lines,
    the more will be the area obtained.

    """

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        area = 0
        i = 0
        j = len(height) - 1

        while i < j:
            current = min(height[i], height[j]) * (j - i)
            area = max(area, current)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

# print(Solution().maxArea([1,2,3,4,5,6,7,8,9,10])) # 25

# print(Solution().maxArea([1,8]))