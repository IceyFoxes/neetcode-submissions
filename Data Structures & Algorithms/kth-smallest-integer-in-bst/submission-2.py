# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        stack = []
        flat = []

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            flat.append(current.val)
   
            current = current.right
        
        return flat[k - 1]
