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

    def __str__(self):
        return str(self.value)

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



class BTreeIterator(object):

    def __init__(self, root):
        self.stack = []
        self.idx = 0

        self._rightmost_inorder(root)


    def _rightmost_inorder(self, root):


        if root:
            next = root.left
            root.left = None

            self._rightmost_inorder(next)

            self.stack.append(root)













    def next(self):
        """
        @return the next smallest number
        """

        # Node at the top of the stack is the next smallest element


        while self.stack and (self.stack[-1].left or self.stack[-1].right):
            topmost_node = self.stack.pop(0)

            topmost_node = topmost_node.right
            aux = []
            # while topmost_node:
            #     next = topmost_node.left
            #     topmost_node.left = None
            #
            #     self._rightmost_inorder(next)
            #
            #     aux.append(topmost_node)
            #
            #
            # self._rightmost_inorder(topmost_node)


        if self.stack:
            return self.stack.pop().value

        return None


    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

tree = BTree(6)
tree.insert(4)
tree.insert(9)
tree.insert(7)
tree.insert(2)
tree.insert(5)



it = BTreeIterator(tree)
while it.hasNext():
    print(it.next())