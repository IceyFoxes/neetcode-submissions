# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, ans = 0, None

        def inorder(node):
            nonlocal count, ans
            if not node or ans is not None:   # found already: stop exploring
                return
            inorder(node.left)
            if ans is not None:               # found inside the left subtree
                return
            count += 1
            if count == k:
                ans = node.val
                return
            inorder(node.right)

        inorder(root)
        return ans