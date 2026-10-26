# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # traverse tree level-order and figure out which one is rightmost

        # use bfs to figure out level

        queue = deque([root])
        res = []
        if not root:
            return res
             
        while queue:
            # level pop
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                val = node.val
            res.append(node.val)
        
        return res

