# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(root, subRoot):
            if root and subRoot:
                return root.val == subRoot.val and check(root.left, subRoot.left) and check(root.right, subRoot.right)
            
            else:
                return root == subRoot
        
        if root:
            if check(root, subRoot):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False