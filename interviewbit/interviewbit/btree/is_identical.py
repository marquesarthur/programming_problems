class Btree(object):

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def add(self, value):
        if value < self.value:
            if not self.left:
                self.left = Btree(value)
            else:
                self.left.add(value)
        else:
            if not self.right:
                self.right = Btree(value)
            else:
                self.right.add(value)


    def in_order(self):

        if self.left:
            self.left.in_order()

        print(self.value)

        if self.right:
            self.right.in_order()


def isIdentical(A, B):
    if not A or not B:
        return False

    a = A.value
    b = B.value

    r = a == b
    if A.left or B.left:
        r = r and isIdentical(A.left, B.left)

    if A.right or B.right:
        r = r and isIdentical(A.right, B.right)

    return r



A = Btree(2)
B = Btree(2)
A.add(1)
B.add(1)
A.add(3)
B.add(3)


# print("A")
# A.in_order()
#
# print("B")
# B.in_order()


print(isIdentical(A, B))

B.add(3)
print(isIdentical(A, B))
