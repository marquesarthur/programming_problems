from leetcode.btree.binary_tree import BTree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter


class Solution(object):

    def traverse(self, node, values):
        if node:
            values.append(node.val)

            self.traverse(node.left, values)
            self.traverse(node.right, values)

    def traverse_replace(self, node, greater_than):
        if node:
            node.val = greater_than[node.val]

            self.traverse_replace(node.left, greater_than)
            self.traverse_replace(node.right, greater_than)

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        values = list()
        self.traverse(root, values)

        values = sorted(values)

        c = Counter(values)
        greater_than = {}
        current_sum = 0
        for k in sorted(c.keys(), reverse=True):
            current_sum += c[k] * k
            greater_than[k] = current_sum

        self.traverse_replace(root, greater_than)
        return root












tree = BTree(4)
tree.insert(1)
tree.insert(0)
tree.insert(2)
tree.insert(6)
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(8)




print(Solution().bstToGst(tree))