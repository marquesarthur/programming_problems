class Tree(object):

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


    def insert(self, node):
        if node < self.val:
            if self.left:
                self.left.insert(node)
            else:
                self.left = Tree(node)
        elif self.right:
            self.right.insert(node)
        else:
            self.right = Tree(node)


    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.val)
        if self.right:
            self.right.in_order()


    def height(self):
        if not self.left and not self.right:
            return 1

        right = 0
        left = 0
        if self.left:
            left = self.left.height()

        if self.right:
            right = self.right.height()

        return 1 + max(left, right)


    def flatten(self):
        if not self.left and not self.right:
            return [self.val]

        result = []

        if self.left:
            result += self.left.flatten()

        result += [self.val]

        if self.right:
            result += self.right.flatten()

        return result



#     10
#    /  \
#   6     15
#  / \     \
# 4   8     36


t = Tree(10)
t.insert(6)
t.insert(15)
t.insert(36)
t.insert(4)
t.insert(8)

#
# t.in_order()
#
# print(t.height())
print(t.flatten())
