# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # let p be smaller than q WLOG:
        if p.val > q.val:
            p, q = q, p
        
        # if q < root, then both are on the left side
        # if p > root, then both are on the right side
        # if q > root but p < root, then that's the LCA
        # if either == root, then that's the LCA
        # basically that's the else case

        while root:
            if q.val < root.val:
                root = root.left
            elif p.val > root.val:
                root = root.right
            else:
                return root
            