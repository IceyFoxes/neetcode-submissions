# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # ignoring trivial cases of negative sums/values
        # at each node, the possible max path sum is either itself + 2 children
        # or itself + 1 child + propagate the sum to its parent

        # therefore, at each node, it has to store the candidate sum of (itself + 2 children) while propagating the max possible sum that uses <= 1 child subtree

        # we use DFS to traverse the tree and compute 2 values: candidate sum, and max sum to be propagated
        max_candidate = root.val

        def dfs(node):
            nonlocal max_candidate
            if node is None:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # this is >= 1 child + self due to the normalizing max(0, ) earlier
            candidate_sum = left + right + node.val

            # compare candidate_sum
            max_candidate = max(candidate_sum, max_candidate)
            max_sum = node.val + max(left, right)

            return max_sum

        dfs(root)
        return max_candidate



