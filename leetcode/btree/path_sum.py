class Solution:
    
    def path(self, root, sum, current):
        if not root:
            return False
        elif current + root.val == sum:
            if not root.left and not root.right:
                return True
            else:
                return self.path(root.left, sum, current + root.val) or self.path(root.right, sum, current + root.val)
        else:
            return self.path(root.left, sum, current + root.val) or self.path(root.right, sum, current + root.val)
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.path(root, sum, 0)

