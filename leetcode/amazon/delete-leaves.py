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

    @staticmethod
    def _children(idx, arr):
        if idx >= len(arr):
            return None

        if arr[idx] == None:
            return None

        t = Tree(arr[idx])
        t.left = Tree._children(idx * 2 + 1, arr)
        t.right = Tree._children(idx * 2 + 2, arr)

        return t

    @staticmethod
    def parse(arr):
        t = Tree(arr[0])
        t.left = Tree._children(0*2 + 1, arr)
        t.right = Tree._children(0*2 + 2, arr)

        return t




LEFT = -1
RIGHT = 1
class Solution(object):

    def is_leaf(self, root):
        if root.left or root.right:
            return False
        return True

    def depth_first_search(self, root, target, aux):
        if not root:
            return

        if root.left and root.left.val == target:
            aux.append((root, LEFT))

        if root.right and root.right.val == target:
            aux.append((root, RIGHT))

        self.depth_first_search(root.left, target, aux)
        self.depth_first_search(root.right, target, aux)

    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """

        # 1 depth first search finding potential targets and their parents
        # iterate array with node, parent, check if leaves and repeat

        stack = []
        self.depth_first_search(root, target, stack)

        if not stack: # no deletions
            return root

        while stack:
            current = stack.pop()

            if current[1] == LEFT and self.is_leaf(current[0].left):
                current[0].left = None

            elif current[1] == RIGHT and self.is_leaf(current[0].right):
                current[0].right = None

        if root.val == target and not root.left and not root.right:
            return None

        return root



t = Tree.parse([1,2,3,2,None,2,4])
# t.in_order()

print("A")
z = Solution().removeLeafNodes(t, 2)
z.in_order()




t = Tree.parse([1,3,3,3,2])
# t.in_order()

print("B")
z = Solution().removeLeafNodes(t, 3)
z.in_order()



t = Tree.parse([1,2,None,2,None,2])
# t.in_order()

print("C")
z = Solution().removeLeafNodes(t, 2)
z.in_order()



t = Tree.parse([1,1,1])
# t.in_order()

print("D")
z = Solution().removeLeafNodes(t, 1)
z.in_order()



