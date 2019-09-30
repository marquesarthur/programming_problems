from leetcode.btree.binary_tree import BTree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def tilt_sum(self, root):
        if not root:
            return 0, 0

        sum_left, tilt_left = self.tilt_sum(root.left)
        sum_right, tilt_right = self.tilt_sum(root.right)

        return root.val + sum_left + sum_right, abs(sum_left - sum_right) + tilt_left + tilt_right

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        sum_left, tilt_left = self.tilt_sum(root.left)
        sum_right, tilt_right = self.tilt_sum(root.right)

        return abs(sum_left - sum_right) + tilt_left + tilt_right




#
# tree = BTree(6)
# tree.insert(4)
# tree.insert(9)
# tree.insert(7)
# tree.insert(11)
# tree.insert(2)
# tree.insert(1)
# tree.insert(4)
# tree.insert(5)



tree = BTree(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)




print(Solution().findTilt(tree))