from leetcode.btree.binary_tree import BTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if val == root.value:
            return root

        if val < root.value:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


tree = BTree(6)
tree.insert(4)
tree.insert(9)
tree.insert(7)
tree.insert(11)
tree.insert(2)
tree.insert(1)
tree.insert(4)
tree.insert(5)


print(Solution().searchBST(tree, 4))
print(Solution().searchBST(tree, 25))