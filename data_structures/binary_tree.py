class BNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BTree(object):

    def __init__(self, value):
        self.root = BNode(value)


    def insert(self, value):
        node = BNode(value)
        self.__insert_node(self.root, node)

    def __insert_node(self, current_node, to_be_inserted):
        if current_node.value > to_be_inserted.value:
            if not current_node.left:
                current_node.left = to_be_inserted
            else:
                current_node = current_node.left
                self.__insert_node(current_node, to_be_inserted)
        else:
            if not current_node.right:
                current_node.right = to_be_inserted
            else:
                current_node = current_node.right
                self.__insert_node(current_node, to_be_inserted)

    def in_order(self):
        self.__walk_in_order(self.root)


    def __walk_in_order(self, current_node):
        if current_node.left:
            self.__walk_in_order(current_node.left)

        print(current_node.value)
        if current_node.right:
            self.__walk_in_order(current_node.right)

    def pre_order(self):
        self.__walk_in_pre_order(self.root)

    def __walk_in_pre_order(self, current_node):
        if current_node.left:
            self.__walk_in_pre_order(current_node.left)
        if current_node.right:
            self.__walk_in_pre_order(current_node.right)
        print(current_node.value)

    def height(self):
        return self.__height(self.root)

    def diameter(self):
        # diameter from current node to current node is 0
        # diameter from left to current node is 1
        # diameter from right to current node is also 1
        return self.__diameter(self.root)

    def __diameter(self, current_node):
        if not current_node:
            return 0

        left = self.__height(current_node.left)
        right = self.__height(current_node.right)

        return max(
            1 + left + right,
            max(self.__diameter(current_node.left), self.__diameter(current_node.right))
        )

        #    6
        #   / \
        #  3   9
        #     /
        #    7



    def __height(self, current_node):
        if not current_node:
            return 0
        else:
            return 1 + max(self.__height(current_node.left), self.__height(current_node.right))



tree = BTree(6)
tree.insert(4)
tree.insert(9)
tree.insert(7)
tree.insert(11)
tree.insert(2)
tree.insert(1)
tree.insert(4)
tree.insert(5)

# After all insertions, we have:
#
#             6
#           /   \
#         4       9
#       /   \       \
#     2      7       11
#   /   \
# 1       4
#           \
#             5
#
# height: 5
# diameter: 6 (from node 5 to node 11)

# tree.in_order()
print(tree.height())
print(tree.diameter())
