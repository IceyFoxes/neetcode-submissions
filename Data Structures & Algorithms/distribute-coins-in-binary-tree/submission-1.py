# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        moves = 0

        def dfs(node):
            nonlocal moves
            if not node:
                return 0
            coins = node.val
            left_need = dfs(node.left)
            right_need = dfs(node.right)
            coins_needed = left_need + right_need - coins + 1
            # add moves here
            moves += abs(left_need) + abs(right_need)
            return coins_needed

        dfs(root)
        return moves


        # dfs and distribute
        # for each node, dfs down first
        # and find how many are unsatisfied
        # and we can calculate the distance for each for a total distance too
        # so each node records down how many nodes want, how far they are (these combine into moves), and how many it itself need, so that gets translated upward to the root
        # if it has excess, then again the root itself has its own wants converted into moves






