# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path, q_path = [], []

        # find paths to both nodes
        def traverse(node, target, path):
            if node is None:
                return False
            
            path.append(node)
            
            if node is target:
                return True
            
            if traverse(node.left, target, path):
                return True
            
            if traverse(node.right, target, path):
                return True

            path.pop()
            return False

        traverse(root, p, p_path)
        traverse(root, q, q_path)

        res = None
        for node1, node2 in zip(p_path, q_path):
            if node1 != node2:
                break
            res = node1
        return res




        # then O(n) iterate from the start (until first divergence)