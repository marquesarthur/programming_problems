# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict


class Solution(object):

    def __visit(self, current, levels, lvl):
        if current:

            if lvl not in levels:
                levels[lvl] = (0, 0)  # sum and num of elements

            levels[lvl] = (levels[lvl][0] + current.val, levels[lvl][1] + 1)

            self.__visit(current.left, levels, lvl + 1)
            self.__visit(current.right, levels, lvl + 1)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = defaultdict(tuple)  # less memory
        self.__visit(root, levels, 0)

        result = []
        for lvl in sorted(levels.keys()):
            x, y = levels[lvl]
            result.append(x / float(y))

        return result



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)


Solution().averageOfLevels(root)