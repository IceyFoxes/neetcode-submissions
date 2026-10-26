# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDiameter = 0

        def traverse(root):
            nonlocal maxDiameter

            if root:
                left = traverse(root.left)
                right = traverse(root.right)
                maxDiameter = max(maxDiameter, left + right)
                return max(left, right) + 1

            return 0
        
        traverse(root)
        return maxDiameter