# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # carry min max down as u traverse

        # DFS
        min_val = float('-inf')
        max_val = float('inf')
        stack = [(root, min_val, max_val)]
        while stack:
            node, min_val, max_val = stack.pop()
            if node.left:
                new_max_val = node.val
                if node.left.val >= new_max_val or node.left.val <= min_val:
                    return False
                stack.append((node.left, min_val, new_max_val))

            if node.right:
                new_min_val = node.val
                if node.right.val >= max_val or node.right.val <= new_min_val:
                    return False
                stack.append((node.right, new_min_val, max_val))
        
        return True
