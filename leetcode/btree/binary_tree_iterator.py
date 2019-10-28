# Definition for a binary tree node.
class BTree(object):

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insert(self, value):
        self.__insert_node(self, value)

    def __insert_node(self, current_node, value):
        if current_node.val > value:
            if not current_node.left:
                current_node.left = BTree(value)
            else:
                current_node.left.insert(value)
        else:
            if not current_node.right:
                current_node.right = BTree(value)
            else:
                current_node.right.insert(value)

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """

        self.stack = []
        self.__visit(root)


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        result = self.stack.pop()
        if result.right:
            self.__visit(result.right)

        return result.val


    def __visit(self, current):
        while current:
            self.stack.append(current)
            current = current.left

    def hasNext(self):
        return self.stack and len(self.stack) > 0






# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



tree = BTree(6)
tree.insert(4)
tree.insert(9)
tree.insert(7)
tree.insert(2)
tree.insert(5)



#        6
#      /   \
#     4     9
#    / \   /
#   2   5 7



it = BSTIterator(tree)
while it.hasNext():
    print(it.next())