# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder = CLR
        # inorder = LCR
        # inorder --> C always in the middle
        inorder_positions = {value: i for i, value in enumerate(inorder)}
        preorder_positions = {value : i for i, value in enumerate(preorder)}

        def recursive_helper(preorder_start, preorder_end, inorder_start, inorder_end):
            # build a binary tree from the top (in a sense C, then its children --> then cursive)
            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None

            node = TreeNode()
            node.val = preorder[preorder_start]

            # find index in inorder that corresponds to the split
            # such that we can pass both halves into the recursion
            inorder_centre = inorder_positions[node.val]

            # we find the index in preorder that matches the first number in the split inorder halves
            preorder_left_start = preorder_start + 1
            preorder_left_size = inorder_centre - inorder_start
            preorder_left_end = preorder_left_start + preorder_left_size - 1

            preorder_right_start = preorder_left_end + 1
            preorder_right_end = preorder_end

            node.left = recursive_helper(preorder_left_start, preorder_left_end, inorder_start, inorder_centre - 1)
            node.right = recursive_helper(preorder_right_start, preorder_right_end, inorder_centre + 1, inorder_end)

            return node

        return recursive_helper(0, len(preorder) - 1, 0, len(inorder) - 1)
