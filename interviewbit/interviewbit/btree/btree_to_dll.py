class Node(object):

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.head = None

    def add(self, value):
        if value < self.value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.add(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.add(value)

    def in_order(self):

        if self.left:
            self.left.in_order()

        print(self.value)

        if self.right:
            self.right.in_order()

    def pre_order(self):

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

        print(self.value)


class BinaryTree:
    root, head = None, None

    # A simple recursive function to convert a given
    # Binary tree to Doubly Linked List
    def to_dll(self, root):
        if root is None:
            return

        # Recursively convert right subtree
        self.to_dll(root.right)

        # Insert root into doubly linked list
        root.right = self.head

        # Change left pointer of previous head
        if self.head is not None:
            self.head.left = root

            # Change head of doubly linked list
        self.head = root

        # Recursively convert left subtree
        self.to_dll(root.left)

    # A = Btree(10)
# A.add(6)
# A.add(4)
# A.add(8)
# A.add(15)
# A.add(13)


B = Node(6)
B.add(4)
B.add(3)
B.add(5)
B.add(7)


A = BinaryTree()
A.root = B

A.to_dll(A.root)


h = A.head

r = ""
while h is not None:
    r += " " + str(h.value) + " -- "
    h = h.right

r += "null"
print(r)

# (a) Inorder (Left, Root, Right) : 3? 4? 5 6 7
# (b) Preorder (Root, Left, Right) : 6 4? 3? 5 7
# (c) Postorder (Left, Right, Root) : 3? 5 4? 7 6
