# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # DFS and just stop early when a node.val > root.val

        max_val = root.val
        stack = [(root, max_val)]
        count = 0

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                max_val = node.val
                count += 1
            
            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))
        
        return count