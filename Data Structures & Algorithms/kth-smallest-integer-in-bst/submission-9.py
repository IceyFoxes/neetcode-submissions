# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def inorder(node):
            nonlocal count
            if not node:
                return None
            left = inorder(node.left)
            if left is not None:
                return left
            count += 1
            if count == k:
                return node.val
            right = inorder(node.right)
            if right is not None:
                return right

        return inorder(root)