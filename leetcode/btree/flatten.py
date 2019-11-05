# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):


    def insert_into(self, root, sub_tree):
        current = root
        while current.right:
            current = current.right

        current.right = sub_tree


    def swap(self, root):
        if not root:
            return

        left = root.left
        right = root.right
        # no left and right:
        if not left and not right:
            return
        # has left and right
        if left and right:
            root.left = None
            self.insert_into(left, right)
            root.right = left
            self.swap(root.right)
        # has left but no right
        elif left and not right:
            root.left = None
            root.right = left
            self.swap(root.right)
        # has no left and right
        elif not left and right:
            self.swap(root.right)
        else:
            return




    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        # idea = if has left pick node to the right and insert it at left tree
        # pick left tree and move to right
        # repeat

        self.swap(root)




#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)


Solution().flatten(root)