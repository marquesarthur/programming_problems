# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    
    def traverse(self, queue, height_nodes):
        while queue:
            root, current = queue.pop(0)

            if root:
                height_nodes[current].append(root)

                if root.left:
                    queue.append((root.left, current + 1))

                if root.right:
                    queue.append((root.right, current + 1))

        
        
        
        
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        height_nodes = defaultdict(list)
        queue = []
        queue.append((root, 0))
        self.traverse(queue, height_nodes)
        
        result = []
        
        if height_nodes.keys():
            for i in range(0, max(height_nodes.keys()) + 1):
                if i in height_nodes:
                    result.append(height_nodes[i].pop().val)
                
        return result
            
        
        
        
