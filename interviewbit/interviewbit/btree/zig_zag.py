# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict

class Solution(object):

    def breadth_first_search(self, stack, nodes_per_height):

        max_h = 0
        while stack:

            root, h = stack.pop(0)

            max_h = max(max_h, h)
            nodes_per_height[h].append(root.val)

            if root.left:
                stack.append((root.left, h + 1))

            if root.right:
                stack.append((root.right, h + 1))


        return max_h









    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        # add nodes to tree in breadth first search
        nodes_per_height = defaultdict(list)


        stack = []
        stack.append((root, 0))

        #walk trough output and invert odd
        max_h = self.breadth_first_search(stack, nodes_per_height)



        for i in xrange(max_h + 1):
            if i % 2 == 0:
                result.append(nodes_per_height[i])
            else:
                result.append(nodes_per_height[i][::-1])

        return result










#     1
#    / \
#   2   5
#  / \   \
# 1   4   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(-1)
root.left.left.right = TreeNode(2)


print(Solution().zigzagLevelOrder(root))