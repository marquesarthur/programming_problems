# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
class BTree(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        self.__insert_node(self, value)

    def __insert_node(self, current_node, value):
        if current_node.value > value:
            if not current_node.left:
                current_node.left = BTree(value)
            else:
                current_node.left.insert(value)
        else:
            if not current_node.right:
                current_node.right = BTree(value)
            else:
                current_node.right.insert(value)

    def in_order(self):
        if self.left:
            self.left.in_order()

        print(self.value)

        if self.right:
            self.right.in_order()

    # The height of a node is the number of edges from the node to the deepest leaf
    def height(self):
        left = self.left.height() if self.left else 0
        right = self.right.height() if self.right else 0
        return 1 + max(left, right)

    def diameter(self):
        # diameter from current node to current node is 0
        # diameter from left to current node is 1
        # diameter from right to current node is also 1
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        left_diameter = self.left.diameter() if self.left else 0
        right_diameter = self.right.diameter() if self.right else 0

        return max(
            1 + left_height + right_height,
            max(left_diameter, right_diameter)
        )



def lca(root, n1, n2):
    if root is None:
        return None

    if root.value > n1 and root.value > n2:
        return lca(root.left, n1, n2)

    if root.value < n1 and root.value < n2:
        return lca(root.right, n1, n2)

    return root



# After all insertions, we have:
#
#             6
#           /   \
#         4       9
#       /   \    /   \
#     2      5  7     11
#   /   \
# 1       4
#
# height: 5
# diameter: 6 (from node 5 to node 11)
tree = BTree(6)
tree.insert(4)
tree.insert(9)
tree.insert(7)
tree.insert(11)
tree.insert(2)
tree.insert(1)
tree.insert(4)
tree.insert(5)

print("""
             6
           /   \\
         4       9
       /   \\    / \\
     2      5  7    11
   /   \\
 1       4
""")
print("lca(tree, 1, 5) = %s" % lca(tree, 1, 5).value)
print("lca(tree, 9, 11) = %s" %lca(tree, 9, 11).value)
print("lca(tree, 1, 7) = %s" %lca(tree, 1, 7).value)
print("lca(tree, 7, 9) = %s" %lca(tree, 7, 9).value)